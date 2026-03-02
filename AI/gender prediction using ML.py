import requests

name = input("Name: ")

url = f"https://api.genderize.io/?name={name}"

response = requests.get(url)
data = response.json()

print(f"Seems like {data['name']} is {data['gender']} and data points used are {data['count']}")