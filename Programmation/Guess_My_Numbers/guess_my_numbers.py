import socket

HOST = 'c.unitedctf.ca'
PORT = 10007

def find_number(data, level):
    num1, num2 = int(data[0]), int(data[1])
    count = num2 - num1
    count2 = int(data[2]) - int(data[1])
    last = int(data[-1])
    output = ""
    if level == "1":
        for _ in range(10):
            last += count
            output += str(last) + ','
    elif level == "2":
        for _ in range(3):
            last += count
            output += str(last) + ','
            last += count2
            output += str(last) + ','
            last *= 10
            output += str(last) + ','
        last += count
        output += str(last) + ','
    elif level == "3":
        for _ in range(10):
            if last % 2 == 0:
                last /= 2
            else:
                last = (last + 4294967295 )/2
            output += str(int(last)) + ','
    output = output[:-1]
    return output

def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            data = s.recv(1024).decode()
            if 'Niveau' in data:
                numbers = data.split(': [')[1].split(']\n')[0].strip()
                list_numbers = numbers.split(',')
                level = data.split('Niveau ')[1].split(':')[0]
                result = find_number(list_numbers, level)
                s.send((result + '\n').encode())
            elif 'flag' in data:
                flag = data.split('Voici votre récompense: ')[1].split('\n')[0].strip()
                print(f"Flag: {flag}")
                break
            elif data == '':
                print("No data received. Exiting.")
                break

if __name__ == "__main__":
    server()