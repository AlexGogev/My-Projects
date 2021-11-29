numbers = [1,2,3,4,5]

numb_plus_one = [i + 1 for i in numbers ]
print(numb_plus_one)

name = "Alex"

cap_name = [i.upper() for i in name]
print(cap_name)

number = [i*2 for i in range(0,100, 3)]
print(number)

number = [i for i in range(0,20) if i % 2 == 0]
print(number)



names = ["Alex", "Ali", "Mama", "Mimi_The_Cat"]
short_names = [i.upper() for i in names if len(i) < 5]
print(short_names)