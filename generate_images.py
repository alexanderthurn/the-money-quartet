import openai
import os
import json

# OpenAI-API-Schlüssel (ersetzen Sie durch Ihren eigenen Schlüssel)
openai.api_key = "YOUR_API_KEY"

# JSON-Datei mit den Währungen
json_file = "currencies_temp.json"

# Verzeichnis für generierte Bilder
output_dir = "generated_images"
os.makedirs(output_dir, exist_ok=True)

# Prompts iterativ verarbeiten
with open(json_file, "r") as file:
    currencies = json.load(file)

    for currency in currencies:
        id = currency["id"]
        name = currency["name"]
        prompt = f"A high-quality flat design icon of {name}, with a white background, simple and minimalistic style."

        print(f"Generating image for {name} (ID: {id})...")

        # API-Aufruf für Bildgenerierung
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="512x512"
        )

        # Bild-URL aus der API-Antwort
        image_url = response["data"][0]["url"]

        # Herunterladen und Speichern des Bildes
        image_path = os.path.join(output_dir, f"{id}_{name.replace(' ', '_')}.png")
        with open(image_path, "wb") as img_file:
            img_file.write(requests.get(image_url).content)

        print(f"Image for {name} saved to {image_path}")
