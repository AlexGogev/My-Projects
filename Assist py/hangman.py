import random
words = ["word", "word2"]

chocen_word = random.choice(words).lower()


display = []
word_len = len(chocen_word)
for i in range(word_len):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    
    guess = input("enter letter: ").lower()
    
    for pos in range(word_len):
        letter = chocen_word[pos]
        if letter == guess:
            display[pos] = letter
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win!")
 
        
