import requests

api_character = "https://rickandmortyapi.com/api/episode/28/?name=rick"

response = requests.get(api_character)
data = response.json()

characters = data["characters"]
rick_characters = []

for character_url in characters:
    character_response = requests.get(character_url)

    character_data = character_response.json()

    if "Rick" in character_data["name"]:
        rick_characters.append(character_data["name"])

if rick_characters:
    print("Characters with 'Rick' in their name from episode 28:")
    for character_name in rick_characters:
        print("-", character_name)
else:
    print("No characters with 'Rick' in their name found in episode 28.")