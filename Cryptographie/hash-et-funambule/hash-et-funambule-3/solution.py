import os
import socket

HOST = 'c.unitedctf.ca'
PORT = 10003

def hashcat():
    os.popen("hashcat -a 0 -m 20 pass.txt rockyou.txt").read()
    result = os.popen("hashcat -a 0 -m 20 pass.txt rockyou.txt --show").read()
    password = result.split(":")[2].strip()
    return password

def interact_with_server():
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
                hash_part = data.split(' : ')[1].split('. ')[0]
                print(f"Hash requested: {hash_part}")

                salt = hash_part.split(':')[0]
                hash = hash_part.split(':')[1]
                all = hash + ":" + salt
                
                with open('pass.txt', 'w') as f:
                    f.write(all)

                # password =  password_from_file(hash_part)
                password = hashcat()
                if '$HEX' in password:
                    password = decrypt_password(password.split('$HEX[')[1].split(']')[0])

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

def decrypt_password(hex_password):
    decoded_password = bytes.fromhex(hex_password).decode('utf-8')
    return decoded_password

if __name__ == "__main__":
    interact_with_server()    