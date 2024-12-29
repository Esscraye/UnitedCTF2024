import socket
import json
from collections import defaultdict
import os


def init_emojis():
    groupe1 = ['😀','🦨','😉','🦔','😜','😨']
    groupe2 = ['🥲','🦐','😡','📎','🥸']
    groupe3 = ['🤣','👾','😰','🦩','😈']
    return groupe1, groupe2, groupe3

def recv_all(sock, buffer_size=1000):
    data = b''
    while True:
        part = sock.recv(buffer_size)
        data += part
        if len(part) < buffer_size:
            break
    return data

def init_json(num_file):
    global groupe1, groupe2, groupe3
    init_emojis()
    data_json = {}
    for i in all_emojis:
        if i in groupe1:
            data_json[i] = ['G1']
        elif i in groupe2:
            data_json[i] = ['G2']
        elif i in groupe3:
            data_json[i] = ['G3']
        else:
            data_json[i] = ['G1', 'G2', 'G3']
    with open(f'etats{num_file}.json', 'w') as f:
        json.dump(data_json, f)

def find_parc_with_3_emojis(emojis):
    solutions = []
    for i in range(len(emojis)):
        positives = [x for x in emojis[i] if x in groupe1]
        negatives = [x for x in emojis[i] if x in groupe2]
        neutrals = [x for x in emojis[i] if x in groupe3]
        if positives and negatives and neutrals:
            solutions.append(i)
    if len(solutions) > 0:
        return solutions[0]
    return -1

def get_flag():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            try:
                data = recv_all(s).decode()
            except:
                return
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

def get_emojis(num):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        try:
            data = recv_all(s).decode()
        except:
            return
        if '100' in data:
            emojis = []
            for i in range(100):
                emojis.append(str(data).split(f'{i+1}: ')[1].split('\n')[0])
            edit_json(emojis, num)
            s.send(('exit \n').encode())

def edit_json(data_set_string, num_file):
    data_set = []
    global groupe1, groupe2, groupe3
    init_emojis()
    for i in data_set_string:
        data_set.append(i.split())
    for i in data_set:
        knowns = []
        groupes = []
        for j in i:
            if j in groupe1:
                knowns.append(j)
                if 1 not in groupes:
                    groupes.append(1)
            elif j in groupe2:
                knowns.append(j)
                if 2 not in groupes:
                    groupes.append(2)
            elif j in groupe3:
                knowns.append(j)
                if 3 not in groupes:
                    groupes.append(3)
        if len(groupes) > 1:
            with open(f'etats{num_file}.json', 'r') as f:
                etats = json.load(f)
            for j in i:
                if j not in knowns:
                    if 1 not in groupes and 'G1' in etats[j]:
                        etats[j].remove('G1')
                    if 2 not in groupes and 'G2' in etats[j]:
                        etats[j].remove('G2')
                    if 3 not in groupes and 'G3' in etats[j]:
                        etats[j].remove('G3')
            with open(f'etats{num_file}.json', 'w') as f:
                json.dump(etats, f)
  
def builds_groups(num_files):
    groupe1, groupe2, groupe3 = [], [], []
    etats = [None] * num_files
    for i in range(num_files):
        with open(f'etats{i}.json', 'r') as f:
            etats[i] = json.load(f)
    
    emoji_counts = defaultdict(lambda: defaultdict(int))

    for etat in etats:
        for emoji, values in etat.items():
            for value in values:
                emoji_counts[emoji][value] += 1

    most_common_values = {}
    for emoji, counts in emoji_counts.items():
        most_common_value = max(counts, key=counts.get)
        most_common_values[emoji] = most_common_value

    for emoji, value in most_common_values.items():
        if value == "G1":
            groupe1.append(emoji)
        elif value == "G2":
            groupe2.append(emoji)
        elif value == "G3":
            groupe3.append(emoji)
    
    return groupe1, groupe2, groupe3


if __name__ == "__main__":
    HOST = 'c.unitedctf.ca'
    PORT = 10025

    all_emojis = ['😀', '🦨', '😉', '🦔', '😜', '😨', '😊', '😍', '🤖', '🚴', '🥴', '🐸', '😂', '🙂', '😌', '🥸', '🤬', '🦨', '🦫', '🤧', '🪲', '🍭', '😫', '😱', '🥲', '🦐', '😡', '📎', '🥸', '🐉', '😓', '😜', '😁', '🤡', '🦆', '🤮', '😋', '😢', '😏', '😭', '🎃', '🎭', '🦭', '🤢', '🤪', '🐕', '🧸', '🐁', '🤣', '👾', '😰', '🦩', '😈', '😵', '😄', '🥷', '😤', '👻', '🙊', '💅', '🗿', '😎', '😉', '🤗', '😆', '💀', '😥', '🦔', '👺', '😝', '🤕', '🦩']
    groupe1, groupe2, groupe3 = init_emojis()

    num_json_files = 5
    for i in range(num_json_files):
        init_json(i)
        for j in range(5):
            get_emojis(i)
    groupe1, groupe2, groupe3 = builds_groups(num_json_files)
    get_flag()
    for i in range(num_json_files):
        os.remove(f'etats{i}.json')
