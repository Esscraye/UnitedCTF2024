import sqlite3


conn = sqlite3.connect('data_leaked/thrill-sync.db')
cursor = conn.cursor()

cursor.execute("SELECT token FROM tokens")

with open('tokens.txt', 'a') as f:
    for row in cursor:
        f.write(row[0] + '\n')

conn.close()
print('Done')
