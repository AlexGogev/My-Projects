import requests
import json
from html import unescape 
from random import shuffle



total = 0
correct = 0
wrong = 0

url = "https://opentdb.com/api.php?amount=1&category=9&difficulty=easy&type=multiple"
response = requests.get(url=url).json()
choices = []
shuffled = shuffle(choices)
class Question:
    def __init__(self):
        self.answer = unescape(response['results'][0]['correct_answer'])
        self.false_answer = unescape(response['results'][0]['incorrect_answers'])
        self.question = unescape(response['results'][0]["question"])

    def add_to_list(self):    
        choices.append(self.answer)
        choices.append(self.false_answer[0])
        choices.append(self.false_answer[1])
        choices.append(self.false_answer[2])
        

class Start:
    def __init__(self):
        Question().add_to_list()
        print(Question().question)
        print(Question().answer)
        self.user_input = int
        self.index = 1
        for i in choices:
            print(self.index, i)
            self.index +=1 
        self.user_entry()
        self.check_answer()
        
    def user_entry(self):
        self.user_input = int(input("What is the correct answer? "))
        if self.user_input > 4:
            print("enter between 1 and 4")
            self.user_entry()

    def check_answer(self):
        if choices[self.user_input-1] == Question().answer:
            print("**** Correct! **** \n")
            global correct
            correct +=1
            
        else:
            print(choices[self.user_input-1])
            print("**** Wrong the correct answere is ", Question().answer ,"****\n")
            global wrong
            wrong +=1
            
Start()


print(f'Correct: {correct} \nWrong: {wrong}')

