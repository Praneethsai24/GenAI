import requests

name = input("Name: ")

url = f"https://api.nationalize.io/?name={name}"

response = requests.get(url)

data = response.json()

print("Name: ", data["name"])
print("\nPossible Countries")

for country in data["country"]:
    print(
        "country ID: ", country["country_id"],
        "| Probablity: ", country["probability"]
    )