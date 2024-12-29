import socket
import json
import sys

HOST = 'c.unitedctf.ca'
PORT = 10011

def leeter2():
    data_dict = {}
    with open('leet.json', 'r') as f:
        if f.read().strip():
            f.seek(0)
            data_dict = json.load(f)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        decoded_phrase = ""
        for _ in range(50):
            data = s.recv(1024).decode()
            if 'Leet Quote: ' in data:
                phrase = data.split('Leet Quote: ')[1].split('\n')[0].strip()
                if phrase in data_dict:
                    decoded_phrase = data_dict[phrase]
                else:
                    data_dict[phrase] = ''
                    with open('leet.json', 'w') as f:
                        json.dump(data_dict, f)
                s.send((decoded_phrase + '\n').encode())
            if 'flag' in data:
                return data.split("V3 ! ")[1].split('\n')[0].strip()
            if 'B4d r3sp0ns3 !' in data:
                print(decoded_phrase)
                return "failed"

if __name__ == "__main__":
    find = False
    while not find:
        flag = leeter2()
        if flag != "failed":
            print(f"Flag: {flag}")
            find = True
