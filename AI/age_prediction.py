import requests
name = input("Name : ")

url = f"https://api.agify.io/?name={name}"

response = requests.get(url)
data = response.json()

print(f"Ai thinks someone named {data['name']} is around {data['age']} years old")
