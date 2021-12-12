import random
import time

class Dice:
    def __init__(self,name):
        self.name = name
        self.dice_one = random.randint(1, 6)
        self.dice_two = random.randint(1, 6)

    def __str__(self):
        return f'{self.name} -> {self.dice_one}:{self.dice_two}'

    def total(self):
        total = self.dice_two + self.dice_one
        return self.name + " " + str(total) 


names = ["az","ti"]
class_list = []
for i in names:
    class_list.append(Dice(i))

bibo = Dice("bibo")
class_list.append(bibo)
print(class_list[0])


name_dict = {}
for i in class_list:
    name_dict[i.name] = i.total()

print(name_dict["az"])