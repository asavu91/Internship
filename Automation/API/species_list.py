import requests

episode_ids = [22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
api_episode = "https://rickandmortyapi.com/api/episode/"

species_set = set()

for episode_id in episode_ids:
    episode_url = f"{api_episode}/{episode_id}"
    response = requests.get(episode_url)
    episode_data = response.json()
    characters = episode_data.get("characters", [])

    for character_url in characters:
        response = requests.get(character_url)
        character_data = response.json()
        species = character_data.get("species")
        character_type = character_data.get("type")

        if species != "unknown" and character_type != "":
            species_set.add((species, character_type))

print("Species types that appear in Season 3:")
for species, character_type in species_set:
    if species != "Human":
        print(f"{species}: {character_type}")
