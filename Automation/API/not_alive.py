import requests

api_episode = "https://rickandmortyapi.com/api/episode/29"

response = requests.get(api_episode)

episode_data = response.json()

characters = episode_data["characters"]

not_alive_characters = []

for character_url in characters:
    character_response = requests.get(character_url)

    character_data = character_response.json()

    if character_data["status"] != "Alive":
        not_alive_characters.append(character_data["name"])

if not_alive_characters:
    print("Characters who are not alive from episode 29:")
    for character_name in not_alive_characters:
        print("-", character_name)
else:
    print("No characters who are not alive found in episode 29.")
