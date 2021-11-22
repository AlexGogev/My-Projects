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


###########

studen_score = {
    "Harry": 10,
    "alex" :51,
    "bibo": 91,
}

studen_grades = {}
for student in studen_score.keys():
    score = studen_score[student]
    if score > 90:
        studen_grades[student] = "outstanding"
    elif score > 50:
        studen_grades[student] = "good"
    elif score < 15:
        studen_grades[student] = "poor"
    
#print(studen_grades)



travel_log = [
    {"spain": {"city": ["malorka","tenerife","lanzarote"]}},
    {"bulgaria": {"city": ["sf", "pld"]}}

]

def add_city(country,city):
    newdict = {}
    newdict[country] = {f"city: {city}"}
    travel_log.append(newdict)

add_city("france", ["nice","monte"])
print(travel_log)


####################

name = ""
bid = ""
others = True
bidders = {}

while others is True:
    name = input("Name? ")
    bid = int(input("Bid? "))
    
    others_bid = input("anyone else? Y or N ").lower()
    if others_bid == "n":
        others = False
    bidders[name] = bid

    print(bidders)

biggest = max(bidders.values())

for k,v in bidders.items():
    if v == biggest:
        name = k

winner = {}
winner[name] = biggest
print("winner is ", winner)