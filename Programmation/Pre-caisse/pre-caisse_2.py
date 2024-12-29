import socket

HOST = 'c.unitedctf.ca'
PORT = 10027

word_to_number = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
    'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
    'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14,
    'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18,
    'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40,
    'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80,
    'ninety': 90, 'hundred': 100, 'thousand': 1000
}

word_to_symbol = {
    'plus': '+', 'minus': '-', 'times': '*', 'divided': '/',
    'modulo': '%'
}


def calculate(elements, s):
    if elements[1] == '+':
        s.send((str(int(elements[0]) + int(elements[2])) + '\n').encode())
    elif elements[1] == '-':
        s.send((str(int(elements[0]) - int(elements[2])) + '\n').encode())
    elif elements[1] == '*':
        s.send((str(int(elements[0]) * int(elements[2])) + '\n').encode())
    elif elements[1] == '/':
        s.send((str(int(int(elements[0]) / int(elements[2]))) + '\n').encode())

def to_numeric(line):
    words = line.lower().split(' =')[0].split(' ')
    num1, num2 = 0, 0
    symbole = ''
    isNumber1 = True
    for word in words:
        if word in word_to_number:
            scale = word_to_number[word]
            if scale == 1000 or scale == 100:
                if isNumber1:
                    num1 *= scale
                else:
                    num2 *= scale
            else:
                if isNumber1:
                    num1 += scale
                else:
                    num2 += scale
        if word in word_to_symbol:
            isNumber1 = False
            symbole = word_to_symbol[word]
    return [num1, symbole, num2]

def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            data = s.recv(1024).decode()
            if '?' in data:
                elements = to_numeric(data)
                calculate(elements, s)
            elif 'flag' in data:
                print(f"Flag: {data}")
                break
            elif data == '':
                print("No data received. Exiting.")
                break

if __name__ == "__main__":
    server()