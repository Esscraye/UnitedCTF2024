import socket

HOST = 'c.unitedctf.ca'
PORT = 10024

all_emojis = ['😢', '😵', '🤕', '😰', '🤬', '🥸', '😏', '😋', '😭', '😥', '😫', '😜', '😄', '🤢', '👾', '🥲', '🦭', '👻', '👺', '🤮', '🦐', '🤖', '🤡', '😌', '🤗', '😁', '😎', '🤪', '😀', '😍', '💀', '🗿', '🙊', '🤣', '📎', '🦔', '💅', '😆', '😡']
positives_emojis = []
negatives_emojis = []
neutral_emojis = []

def categorize_emojis():
    positives_emojis.extend(['😋', '😜', '😄', '😌', '🤗', '😁', '😎', '🤪', '😀', '😍', '🤣', '😆', '😏'])
    negatives_emojis.extend(['😢', '😵', '🤕', '😰', '🤬', '😭', '😥', '😫', '🤢', '🤮', '😡', '🥲', '💀'])
    neutral_emojis.extend(['🥸', '👾', '🦭', '🦐', '🤖', '🤡', '🗿', '🙊', '📎', '🦔', '💅', '👻', '👺'])


def recv_all(sock, buffer_size=1000):
    data = b''
    while True:
        part = sock.recv(buffer_size)
        data += part
        if len(part) < buffer_size:
            break
    return data

def get_all_emojis_ones(data):
    emojis = []
    for i in data:
        for j in i:
            if j not in emojis:
                emojis.append(j)
    return emojis

def find_parc_with_3_emojis(emojis):
    solutions = []
    for i in range(len(emojis)):
        positives = [x for x in emojis[i] if x in positives_emojis]
        negatives = [x for x in emojis[i] if x in negatives_emojis]
        neutrals = [x for x in emojis[i] if x in neutral_emojis]
        if positives and negatives and neutrals:
            solutions.append(i)
    if len(solutions) > 0:
        return solutions[0]
    return -1


def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        for i in range(11):
            data = recv_all(s).decode()
            if '100' in data:
                emojis = []
                for i in range(100):
                    emojis.append(str(data).split(f'{i+1}: ')[1].split('\n')[0])
                result = find_parc_with_3_emojis(emojis)
                s.send((str(result + 1) + '\n').encode())
            elif 'flag' in data:
                flag = data
                print(f"Flag: {flag}")
                break
            elif data == '':
                print("No data received. Exiting.")
                break

if __name__ == "__main__":
    categorize_emojis()

    server()
    