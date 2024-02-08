import requests

data = "https://rickandmortyapi.com/api/character/?name=Narnia&status=alive"

response = requests.get(data)
character_data = response.json()



characters = character_data.get("results", [])

if characters:
    print("Characters who are alive and appeared in the 'Narnia Dimension':")
    for character in characters:
        print("-", character["name"])
else:
    print("No characters found.")