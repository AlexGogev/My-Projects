import os
list= []
for i in range(1,101):
    list.append(i)
print(list)
dir = "C:/Users/Alex/Desktop/Portfolio Python/"

for i in range(1,101):
    os.mkdir(f'C:/Users/Alex/Desktop/Portfolio Python/Project {i}')

