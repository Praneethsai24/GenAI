import requests
name = input("Name : ")

url = f"https://api.agify.io/?name={name}"

response = requests.get(url) # we send a request to the specifc website or url
data = response.json() # site gives us back Json file. 

print(f"Ai thinks someone named {data['name']} is around {data['age']} years old")
print("Confidence (count of data points):", data["count"]) # the number of data points the model has seen for that name.
# More confidence or Large count means more realible average (stronger prediction)