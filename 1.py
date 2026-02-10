import requests

prompt = "Explain API in on paragraph."

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model":"phi3.5:3.8b",
        "prompt": prompt,
        "stream": False
    }
)

#print(response.json()["response"])

# if response.status_code != 200:
#     print(response.text)
# else:
#     print(response.json()["response"])

print(type(response.text))
print(type(response.json()))