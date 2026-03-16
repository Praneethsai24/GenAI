import requests 
import json


examples = [
    {"text" : "Limited offer", "label" : "spam"},
    {"text" : "You Got a reward, click here", "label" : "spam"},
    {"text" : "Meeting scheduled", "label" : "not spam"},
    {"text" : "Your OPT is", "label" : "not spam"}
]

new_mail = "Congratulations on winning a reward"

prompt = "Classify this email as spam or not spam.\n\n"

for ex in examples :
    prompt += f"Email: {ex['text']}\nLabel: {ex['label']}\n\n"

prompt += f"Email: {new_mail}\nLabel:"

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "phi3.5:3.8b",
        "prompt": prompt,
        "stream": False
    }
)

result = response.json()

print("Model prediction")
print(result["response"])