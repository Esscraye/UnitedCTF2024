from py7zr import SevenZipFile
from itertools import product

find = False
    
while find == False:
    with open('rockyou.txt', 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            # Nettoyer la ligne pour enlever les caractères de fin de ligne
            word = line.strip()
            try:
                archive = SevenZipFile(r'monfichier.7z', mode='r', password = word)
                archive.extractall()
                archive.close()
                find = True
            except:
                print(f"Password incorrect: {word}")
