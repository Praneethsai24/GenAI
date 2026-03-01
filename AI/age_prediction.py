import requests
<<<<<<< HEAD
name = input("Name : ")
=======
name = "Max"
>>>>>>> 3c0572ac386a2a3f761ca2ca1f439dbe28eed405

url = f"https://api.agify.io/?name={name}"

response = requests.get(url)
data = response.json()

<<<<<<< HEAD
print(f"Ai thinks someone named {data['name']} is around {data['age']} years old")
=======
print("Name:", data["name"])
print("Predicted Age:", data["age"])
print("Confidence:", data["count"])
>>>>>>> 3c0572ac386a2a3f761ca2ca1f439dbe28eed405
