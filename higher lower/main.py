from art import logo, vs
from data import data
import random
print(logo)


    
my_score = 0
missed = True
while missed:
    random_data1 = random.choice(data)
    score_1 = random_data1["follower_count"]

    random_data2 = random.choice(data)
    score_2 = random_data2["follower_count"]

    print(f"Compare A: {random_data1['name']}, {random_data1['description']}, from {random_data1['country']}" )
    print(vs)
    print(f"Compare B: {random_data2['name']}, {random_data2['description']}, from {random_data2['country']}" )
    print(score_1,score_2)
    answer = input("Who has more followers 'A' or 'B': ").lower()
    
    if answer == "a" and score_1 > score_2:
        my_score += 1
        print("\n Yes!  \n \n")
    elif answer == "a" and score_1 < score_2:
        print(f"No! You lost! Your score is {my_score}")
        missed = False
    elif answer == "b" and score_1 < score_2:
        my_score += 1
        print("\n Yes! \n \n")
    elif answer == "b" and score_1 > score_2:
        print(f"No! You lost! Your score is {my_score}")
        missed = False
   
    
