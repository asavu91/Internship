import requests

data = "https://rickandmortyapi.com/api/character/"

response = requests.get(data)
data = response.json()

def get_rick_id():
    for character in data["results"]:
        if character["name"] == "Rick Sanchez":
            rick_id = character["id"]
            print("Character ID of Rick Sanchez:", rick_id)
            break
    else:
        print("Failed to find Rick Sanchez in the API data")

get_rick_id()
