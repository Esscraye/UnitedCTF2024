import socket

HOST = 'c.unitedctf.ca'
PORT = 10026

def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            data = s.recv(1024).decode()
            if '?' in data:
                elements = data.split(' ')
                if elements[1] == '+':
                    s.send((str(int(elements[0]) + int(elements[2])) + '\n').encode())
                elif elements[1] == '-':
                    s.send((str(int(elements[0]) - int(elements[2])) + '\n').encode())
                elif elements[1] == '*':
                    s.send((str(int(elements[0]) * int(elements[2])) + '\n').encode())
                elif elements[1] == '/':
                    s.send((str(int(int(elements[0]) / int(elements[2]))) + '\n').encode())
            elif 'flag' in data:
                print(f"Flag: {data}")
                break
            elif data == '':
                print("No data received. Exiting.")
                break

if __name__ == "__main__":
    server()