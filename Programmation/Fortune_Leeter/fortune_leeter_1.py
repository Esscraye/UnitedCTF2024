import socket
import time

HOST = 'c.unitedctf.ca'
PORT = 10010

dico1 = {
    '1': 'l',
    '3': 'e',
    '4': 'a',
    '5': 's',
    '7': 't',
    '0': 'o',
    '9': 'g',
}

dico2 = {
    '/<': 'k',
    '/-\\': 'a',
    '/\\/\\': 'm',
    '/V': 'n',
    '/-/': 'h',
    '/3': 'b',
    '\\X/': 'w',
    '\\|/': 'y',
    '\\/': 'v',
}    

dico3 = {
    '@': 'a',
    '$': 's',
    '1': 'i',
    '¥': 'y',
    '()': 'o',
    '(_)': 'u',
    '/\\/': 'n',
    '€': 'e',
    '|V|': 'm',
    '/2': 'r',
    '£': 'l',
    '\\\\\'': 'w',
    '"|"': 't',
    ')-(': 'h',
    '9': 'g',
    '/=': 'f',
    '\\/': 'v',
    '|)': 'd',
    '|<': 'k',
    '[': 'c',
    '|3': 'b',
    '<|': 'q',
    '|>': 'p',
    '_]': 'j',
    '><': 'x',
}

def decode_leet(phrase):
    decoded_phrase = phrase
    for leet, char in dico.items():
        decoded_phrase = decoded_phrase.replace(leet, char)
    return decoded_phrase

def leeter(level):
    global dico
    dico = dico1 if level == 0 else dico2 if level == 1 else dico3
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            data = s.recv(1024).decode()
            if 'Choose your level of difficulty (from 0 to 2)' in data:
                s.send((f'{level}\n').encode())
                continue
            elif 'Leet Quote: ' in data:
                phrase = data.split('Leet Quote: ')[1].split('\n')[0].strip()
                decoded_phrase = decode_leet(phrase)
                s.send((decoded_phrase + '\n').encode())
            elif 'part of the flag' in data:
                flag = data.split('part of the flag: ')[1].split('\n')[0].strip()
                print(f"Flag: {flag}")
                break
            elif data == '':
                print("No data received. Exiting.")
                break

if __name__ == "__main__":
    for i in range(3):
        leeter(i)
