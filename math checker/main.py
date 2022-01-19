import random


with open("math.txt", "w") as mathtext:
    for i in range(15):
        x = random.randint(1, 12)
        z = 5
        mathtext.write(f'{int(x)} * {int(z)} = \n')


with open("math.txt" , "r", encoding="utf-8") as text:
    text = text.readlines()


clean_list = []
for i in text:
    clean_list.append(i[0:-1])

x = (clean_list)

with open("results.txt", "w") as result:
    for i in clean_list:
        res = eval(i[:-2])
        result.write(f'{str(res)} \n')