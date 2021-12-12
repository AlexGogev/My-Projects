#https://github.com/hermitdave/FrequencyWords/tree/master/content/2018

with open("bulgarian.txt", "r") as text:
    words = text.readlines()

words = "".join(words)


list_words = []
for i in words:
    if i =="1" or i =="2" or i =="3" or i =="4" or i=="5" or i=="6" or i=="7" or i =="8" or i=="9" or i =="0":
        continue
    else:
        list_words.append(i)

list_words = "".join(list_words)


with open("bg.txt", "w") as text:
    text.write(list_words)

