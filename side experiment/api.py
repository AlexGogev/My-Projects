import requests
import json

for i in range(10):
    response = requests.get(url="https://catfact.ninja/fact")
    data = response.json()
    print(data["fact"])