from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
x = [{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},]

question_bank = [
]



for i in question_data:
    question_text = i["text"]
    question_anser = i["answer"]
    new_question = Question(question_text, question_anser)
    question_bank.append(new_question)

#print(question_bank[0].text)


quiz= QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f'Your final score is {quiz.score}/{quiz.question_number}')