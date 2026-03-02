'''
import requests

name = input("Name: ")

url = f"https://api.genderize.io/?name={name}"

response = requests.get(url)
data = response.json()

print(f"Seems like {data['name']} is {data['gender']} and data points used are {data['count']}")
'''
# Here gneder is a Model's Prediction


# We use loop Now!

import requests

results = []

for i in range(5):
    name = input(f"Name {i+1}: ")

    url = f"https://api.genderize.io/?name={name}"
    response = requests.get(url)
    data = response.json()

    results.append(data)
    