class Account:
    def __init__(self, name):
        self.name= name
        self.balance = 0
        self.borowed_to = {}
    
    def add_money(self,value):
        self.balance +=  value

    def print_balance(self):
        print(f'{self.name} has {self.balance} pounds')

    def give(self, person, pounds):
        if self.balance - pounds < 0:
            print("Not enough money")
        else:
            person.balance = pounds
            self.balance -= pounds
            self.borowed_to[person.name] = pounds

    def total_to_collect(self):
        total = 0
        for i in self.borowed_to.values():
            total += i
        print(total)
            
        

        


alex = Account("Alex")
ani = Account("Ani")
baba = Account("Baba")
alex.balance = 100

alex.give(ani, 25)
alex.give(baba, 15)
alex.total_to_collect()

alex.print_balance()

    