with open("math.txt", "r") as completed:
    text = completed.readlines()

ans = []
for i in text:
    ans.append(i.strip("\n"))

completed = []

for i in ans:
    completed.append(i.split('=')[1].lstrip().split(' ')[0])


with open("results.txt", "r") as results:
    res = results.readlines()
results = []
for i in res:
    results.append(i[:-2])

print(completed)
print(results)

n =0

correct = 0
wrong = 0
for i in completed:
    if i == results[n]:
        correct +=1
        n +=1
    else :
        wrong +=1
        n +=1
print(f'correct: {correct} \nwrong: {wrong}')