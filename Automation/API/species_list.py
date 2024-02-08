import requests

episode_ids = [22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
api_episode = "https://rickandmortyapi.com/api/episode/"

species_list = []

for episode_id in episode_ids:
    episode_url = f"{api_episode}{episode_id}"
    response = requests.get(episode_url)
    episode_data = response.json()
    characters = episode_data.get("characters", [])

    for character_url in characters:
        response = requests.get(character_url)
        character_data = response.json()
        species = character_data.get("species")
        character_type = character_data.get("type")
        character_name = character_data.get("name")

        if species and character_type and character_name:
            species_list.append({"species": species, "type": character_type, "name": character_name})

print("Species types that appear in Season 3:")
for species_data in species_list:
    print(f'Species: {species_data["species"]}, Type: {species_data["type"]}, Name: {species_data["name"]}')
