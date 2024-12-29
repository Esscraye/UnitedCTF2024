import socket
import hashlib
import json

# Configurations
HOST = 'c.unitedctf.ca'
PORT = 10002

def password_from_file(HASH):
    # Lire le fichier de mots de passe
    try:
        with open('rockyou.txt', 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                # Nettoyer la ligne pour enlever les caractères de fin de ligne
                word = line.strip()
                # Calculer le hash MD5 du mot de passe
                guess = hashlib.md5(word.encode('utf-8')).hexdigest()
                # Comparer le hash calculé avec le hash recherché
                if guess.upper() == HASH or guess.lower() == HASH:
                    print(f'[+] Password found: {word}')
                    return word
                    #print(f'[-] Guess: {word} incorrect...')
        # Si aucun mot de passe ne correspond
        print('Password not found in wordlist...')
        return None
    except FileNotFoundError:
        print("Le fichier 'rockyou.txt' n'a pas été trouvé.")
        return None
    except Exception as e:
        print(f"Une erreur est survenue: {e}")
        return None
    
def write_all_hashes():
    data = {}
    try:
        with open('rockyou.txt', 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                # Nettoyer la ligne pour enlever les caractères de fin de ligne
                word = line.strip()
                # Calculer le hash MD5 du mot de passe
                guess = hashlib.md5(word.encode('utf-8')).hexdigest()
                data[word] = guess
    except FileNotFoundError:
        print("Le fichier 'rockyou.txt' n'a pas été trouvé.")
        return None
    except Exception as e:
        print(f"Une erreur est survenue: {e}")
        return None
    with open('data.json', 'w', encoding='utf-8', errors='ignore') as file:
        json.dump(data, file)
    print("finished")

def find_password(passwords, hash):
    for word in passwords:
        if passwords[word] == hash:
            return word
    

def md5_hash(data):
    return hashlib.md5(data.encode()).hexdigest()

def interact_with_server(passwords):
    # Créer une connexion au serveur
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        
        # Lire la bienvenue du serveur
        data = s.recv(1024).decode()
        print(f"Server: {data}")
        
        # Choisir la langue (en ou fr)
        lang = 'fr'  # On peut changer cette ligne pour 'fr' si on veut tester avec le français
        s.send((lang + '\n').encode())
        print(f"Sent language: {lang}")
        
        data = s.recv(1024).decode()
        print(f"Server: {data}")
        
        i = 0
        # Interagir avec le serveur
        while i < 1000:
            # Lire la demande du serveur
            # Extraire le hash de la demande
            if 'Voici le hash' in data:
                number = data.split('Voici le hash #')[1].split(' :')[0]
                i = int(number)
            if ' : ' in data:
                hash_part = data.split(' : ')[1].split(' ')[0].split('.')[0]
                print(f"Hash requested: {hash_part}")
                

                # password =  password_from_file(hash_part)
                password = find_password(passwords, hash_part)

                # Calculer le hash du mot de passe

                s.send((password + '\n').encode())
                print(f"Sent password: {password}")
                    
                # Lire la réponse du serveur
                data = s.recv(512).decode()
                print(f"Server response: {data}")
                print(f"i: {i}")
            else:
                data = s.recv(512).decode()
                if data == '':
                    break
                print(f"Server: {data}")
                

        # Lire le flag à la fin
        data = s.recv(1024).decode()
        print(f"Server: {data}") if data else ""

if __name__ == "__main__":
    with open('data.json', 'r', encoding='utf-8', errors='ignore') as file:
        passwords = json.load(file)
        
    interact_with_server(passwords)

    
    # write_all_hashes()
