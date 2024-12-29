# Hash & Funambules - 2

## Solution (échec)

Ce coup-ci à cause du `bcrypt`, comparer en temps réel avec tout rockyou.txt prend beaucoup trop de temps, c'est donc impossible avec la méthode de la version 3.

J'ai donc essayé de hashé à l'avance tous les mots de passe de rockyou.txt en utilisant exactement le même code que selui du serveur (cf le script ci-dessous) malheuresement, les hashs ne correspondaient pas (pas sûr de comprendre pourquoi d'ailleurs...)

Ce qu'il fallait voir que la faille dans le code était que comme `values` est un array de type `byte`, alors `v` va lui aussi être de type `byte` et donc va avoir une valeur comprise entre 0 et 255. Donc le mot de passe se trouvait proche du précédent.

<details>
<summary>Script pour hasher les mots de passe</summary>

```go
package main

import (
	"bufio"
	"crypto/md5"
	"crypto/sha1"
	"crypto/sha256"
	"crypto/sha512"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"hash"
	"log"
	"os"
	"path/filepath"
	"sync"
	"time"

	"golang.org/x/crypto/bcrypt"
	"golang.org/x/crypto/blake2b"
	"golang.org/x/crypto/sha3"
)

func hashPassword(password string, algorithm string) (string, error) {
	var hasher hash.Hash
	switch algorithm {
	case "md5":
		hasher = md5.New()
	case "sha1":
		hasher = sha1.New()
	case "sha256":
		hasher = sha256.New()
	case "sha512":
		hasher = sha512.New()
	case "blake2b":
		var err error
		hasher, err = blake2b.New256(nil)
		if err != nil {
			return "", err
		}
	case "sha3-256":
		hasher = sha3.New256()
	case "sha3-512":
		hasher = sha3.New512()
	case "bcrypt":
		hashedPassword, err := bcrypt.GenerateFromPassword([]byte(password), bcrypt.DefaultCost)
		if err != nil {
			return "", err
		}
		return string(hashedPassword), nil
	default:
		return "", fmt.Errorf("unsupported algorithm: %s", algorithm)
	}

	hasher.Write([]byte(password))
	return hex.EncodeToString(hasher.Sum(nil)), nil
}

func readFile(filename string) ([]string, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines, scanner.Err()
}

func writeJSON(filename string, data map[string]string) error {
	file, err := os.Create(filename)
	if err != nil {
		return err
	}
	defer file.Close()

	encoder := json.NewEncoder(file)
	encoder.SetIndent("", "  ")
	return encoder.Encode(data)
}

func processPart(part string, algorithms []string, wg *sync.WaitGroup, errChan chan error, counterChan chan int) {
	defer wg.Done()

	passwords, err := readFile(part)
	if err != nil {
		errChan <- fmt.Errorf("error reading file %s: %v", part, err)
		return
	}

	for _, algorithm := range algorithms {
		passwordMap := make(map[string]string)
		for _, password := range passwords {
			hashedPassword, err := hashPassword(password, algorithm)
			if err != nil {
				log.Printf("Error hashing password with %s: %v", algorithm, err)
				continue
			}
			passwordMap[hashedPassword] = password
			counterChan <- 1 // Increment the counter for each hashed password
		}
		outputFile := fmt.Sprintf("bcryptoutput/dico_0/%s_%s.json", algorithm, filepath.Base(part))
		if err := writeJSON(outputFile, passwordMap); err != nil {
			errChan <- fmt.Errorf("error writing JSON file for %s: %v", algorithm, err)
		} else {
			log.Printf("Successfully wrote JSON file for %s", algorithm)
		}
	}
}

func main() {
	algorithms := []string{"bcrypt"}
	parts := make([]string, 11)
	for i := 0; i < 11; i++ {
		parts[i] = fmt.Sprintf("rockyou/rockyou_part_0/rockyou_part_%d.txt", i)
	}

	var wg sync.WaitGroup
	errChan := make(chan error, len(parts))
	counterChan := make(chan int, len(parts)*1000) // Buffered channel to avoid blocking

	// Start a goroutine to count and display the number of elements processed every 10 seconds
	go func() {
		ticker := time.NewTicker(10 * time.Second)
		defer ticker.Stop()

		totalCount := 0
		for {
			select {
			case count := <-counterChan:
				totalCount += count
			case <-ticker.C:
				log.Printf("Processed %d elements so far", totalCount)
			}
		}
	}()

	for _, part := range parts {
		wg.Add(1)
		go processPart(part, algorithms, &wg, errChan, counterChan)
	}

	wg.Wait()
	close(errChan)
	close(counterChan)

	for err := range errChan {
		if err != nil {
			log.Println(err)
		}
	}
}
```

</details>