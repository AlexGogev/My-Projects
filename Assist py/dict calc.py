#calculator

def add(n1,n2):
    return n1 +n2

def substract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1 * n2

def devide(n1,n2):
    return n1/n2

operator = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": devide,
    }

num1 = float(input("Enter number: "))
op_simbol = input("enter + - * / ")
num2 = float(input("Enter number: "))

calc_func = operator[op_simbol]
ans = calc_func(num1,num2)
print(ans)