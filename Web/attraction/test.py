import requests
import json

url = "https://onlyparks3.c.unitedctf.ca/api/article"

# Corps de la requête (ajustez selon vos besoins)
payload = {
    "where": {
        "id": 1
    },
    "include": {
        "clowns": True,
    },
}

# Envoyer la requête POST à l'API
response = requests.post(url, json=payload)

# Vérifier si la requête a réussi
if response.status_code == 200:
    # Récupérer la réponse JSON
    data = response.json()

    print("Réponse complète:", json.dumps(data, indent=4))
    
    # Vérifier si la réponse est OK
    if data.get("ok"):
        # Extraire les données de results
        results = data.get("results", [])
        print("Results:", results)
    else:
        print("Erreur dans la réponse:", data.get("error"))
else:
    print("Erreur lors de la requête:", response.status_code)