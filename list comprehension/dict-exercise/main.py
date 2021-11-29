
import random

names = ["Alex","Mama","Ali"]
lucky = {i:random.randint(0,101) for i in names}

print(lucky)

very_lucky = {}

for k , v in lucky.items():
    if v > 50:
        very_lucky[k] = v
print(very_lucky)


very_lucky_comprehension = {k:v for k,v in lucky.items() if v > 50}
print(very_lucky_comprehension)