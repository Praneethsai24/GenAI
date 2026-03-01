import os
import requests
from openai import OpenAI

names = ["Max", "Checo", "Charles", "Sainz"]

agify_url = "https://api.agify.io"

results = []

for name in names:
    r = requests.get(agify_url, params={"name": name})
    information = r.json()
    results.append(f"{information['name']} is likely {information['age']} years old")

prompt = (
    "here are some age predictions: \n"
    + "\n".join(results)
    + "\n\nDescribe these people in a friendly 2-4 sentence paragraph."
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

resp = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [{"role":"user", "content": prompt}]
)

print(resp.choices[0].message["content"])
