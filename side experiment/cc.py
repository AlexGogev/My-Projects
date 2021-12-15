import random

class CC:
    def __init__(self, name):
        self.name = name
        self.account_num = ""
        self.account = self.account()
        

    def account(self):
        acc = []
        for i in range(6):
            acc.append(str(random.randint(1, 9)))
        self.account_num = "".join(acc)

az = CC("me")
print(az.account_num)