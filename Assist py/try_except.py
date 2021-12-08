"""
try:
  #somthing may couse exeption
except:
 #do if there is exeption
else:
 #do this if there is no exeption -> if there is no problems with 'try:'
finally:
 #do this no matter what
"""

try:
    " file not foud "
    with open("file.txt", "r") as data:
        data.read()
        dictionary = {"you":1,"me":2}
        #print(dictionary["hi"])

except FileNotFoundError:
    with open("file.txt", "w") as data:
        data.read()
    
except KeyError:
    print("intex out of range")


else:
    "if try was success"
    print("try code was ok!")




# raise error
height = 3
weight = 55

if height > 3:
    raise ValueError("Cannot be that tall")
print(weight / height **2)





fruits = ["Apple", "Pear", "Orange"]
# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit + " pie") #comment it and move it to else
    except IndexError as error:
        print(f"hi this is {error}")
    else:
        print(fruit + "pie is amazing!")

make_pie(2)






facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for i in facebook_posts:
    try:
        total_likes = total_likes + i['Likes']
    except KeyError:
        print("out of range") # pass
    



print(total_likes)