import requests

api_character = "https://rickandmortyapi.com/api/character/?name=Gene"

response = requests.get(api_character)


data = response.json()

def gene_apperance():
    if data["results"]:
            gene_data = data["results"][0]
            gene_location = gene_data["location"]["name"]
            gene_episodes = gene_data["episode"]
            print("Gene's location:", gene_location)
            print("Gene's episodes:", gene_episodes)
    else:
            print("No character named Gene found.")

gene_apperance()