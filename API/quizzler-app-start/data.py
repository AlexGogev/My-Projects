import requests
import json

#response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean").json()  SAME as below

parameters = {
    "amount":10,
    "type": "boolean",
    "category":27,
    "difficulty":"easy"
}
#category 27 = animals
#category 9 = general knowladge

response = requests.get(url="https://opentdb.com/api.php", params=parameters).json()

question_data = response["results"]

#same as above
"""for i in range(10):
    response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean").json()
    question= response["results"][0]["question"]
    answer = response["results"][0]["correct_answer"]
    question_data.append({"question": question, "correct_answer": answer})

"""

