import requests
import json
from html import unescape 
from random import shuffle

index = 1

total = 0
correct = 0
wrong = 0
user_input = int
def user_entry():
    global user_input

    user_input = int(input("What is the correct answer? "))
    if user_input > 4:
        print("enter between 1 and 4")
        user_entry()

while total < 5:
    url = "https://opentdb.com/api.php?amount=1&category=9&difficulty=easy&type=multiple"
    response = requests.get(url=url).json()

    answer = unescape(response['results'][0]['correct_answer'])
    false_answer = unescape(response['results'][0]['incorrect_answers'])
    question = unescape(response['results'][0]["question"])
    choices = [answer, false_answer[0], false_answer[1], false_answer[2]]
    print(question)
    print("------")
    shuffled = shuffle(choices)

    #print(answer)

    
    for i in choices:
        print(f'{index} {i}')
        index +=1
    user_entry()
    if choices[user_input-1] == answer:
        print("**** Correct! **** \n")
        index = 1
        correct += 1
        total +=1
    else:
        print("**** Wrong the correct answere is ", answer ,"****\n")
        index = 1
        wrong += 1
        total +=1 

print(f'Correct: {correct} \nWrong: {wrong}')


