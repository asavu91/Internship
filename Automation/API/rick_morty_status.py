import requests

data = "https://rickandmortyapi.com/api/character/"

response = requests.get(data)
data = response.json()


rick_status = None
rick_location = None
morty_status = None
morty_location = None

def get_status():
    for character in data["results"]:
        if character["name"] == "Rick Sanchez":
            rick_status = character["status"]
            rick_location = character["location"]["name"]
        elif character["name"] == "Morty Smith":
            morty_status = character["status"]
            morty_location = character["location"]["name"]


    print("Rick Sanchez - Status:", rick_status)
    print("Rick Sanchez - Location:", rick_location)
    print("Morty Smith - Status:", morty_status)
    print("Morty Smith - Location:", morty_location)


get_status()