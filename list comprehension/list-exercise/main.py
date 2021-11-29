
with open("file1.txt") as file1:
    file1 = file1.readlines()
    file_1 = [int(i[0:-1]) for i in file1]
    #print(file_1)


with open("file2.txt") as file2:
    file2 = file2.readlines()
    file_2 = [int(i[0:-1]) for i in file2]
    #print(file_2)

print(sorted(file_1))
print(sorted(file_2))
result = [i for i in file_1 if i == i in file_2]
# Write your code above 👆

print(result)


