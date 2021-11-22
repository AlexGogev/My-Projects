class Animal:
    def __init__(self):
        self.eyes = 2
        print("hi I am animal")
    
    def greet(self):
        print("hello")

class Cat(Animal):
    def __init__(self):
        super().__init__()
            
    def greet(self):
        super().greet()
        print("Meow")

mimi = Cat()
mimi.greet()
