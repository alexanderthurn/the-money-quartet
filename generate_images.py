import requests
import json
import os
import time

# API-Key aus der Datei 'key' auslesen
with open("key", "r") as file:
    api_key = file.read().strip()

# JSON-Datei mit Währungen laden
with open("currencies.json", "r") as file:
    currencies = json.load(file)

# Verzeichnis für generierte Bilder
output_dir = "images"
os.makedirs(output_dir, exist_ok=True)

# URL und Header für die API
url = "https://api.openai.com/v1/images/generations"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Iteration über alle Währungen
for i, currency in enumerate(currencies):
    id = currency["id"]
    name = currency["name"]
    output_path = os.path.join(output_dir, f"{id}_{name.replace(' ', '_')}.png")

    # Überspringen, wenn das Bild bereits existiert
    if os.path.exists(output_path):
        print(f"Image for {name} (ID: {id}) already exists. Skipping...")
        continue

    # Prompt für die Bildgenerierung
    prompt = f"A high-quality flat design icon of {name}, with a white background, simple and minimalistic style."

    print(f"Generating image for {name} (ID: {id})...")

    # Anfrage an die API
    data = {
        "prompt": prompt,
        "n": 1,
        "size": "512x512"
    }
    response = requests.post(url, headers=headers, json=data)

    # Fehlerbehandlung
    if response.status_code != 200:
        print(f"Error generating image for {name}: {response.status_code}, {response.text}")
        continue

    # Bild speichern
    image_url = response.json()["data"][0]["url"]
    image_data = requests.get(image_url).content
    with open(output_path, "wb") as file:
        file.write(image_data)

    print(f"Image for {name} saved as '{output_path}'")

    # Wartezeit einfügen, um das Rate Limit einzuhalten
    if (i + 1) % 5 == 0:  # Nach jeder fünften Anfrage warten
        print("Rate limit reached. Waiting for 60 seconds...")
        time.sleep(60)

print("All images processed successfully!")
