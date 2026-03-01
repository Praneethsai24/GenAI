import requests
name = "Max"

url = f"https://api.agify.io/?name={name}"

response = requests.get(url)
data = response.json()

print("Name:", data["name"])
print("Predicted Age:", data["age"])
print("Confidence:", data["count"])
