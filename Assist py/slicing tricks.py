#https://medium.com/techtofreedom/5-python-slicing-tricks-that-will-make-your-code-more-elegant-bd5e27c73f7

#How to get the first 3 items
a = [1, 2, 3, 4, 5, 6]
a[:3]  # [1, 2, 3]

#How to get the last 3 items
a[-3:]

#Take Every Nth Item of a List
a[::2]
[1, 3, 5]

#A commonly used trick is to reverse a list as follows:
a[::-1]
[6, 5, 4, 3, 2, 1]


#Shallow Copy a List
b = a[:]
b[0] = 100  # b  -> [100, 2, 3, 4, 5, 6]

#Assign multiple items at once
a[:3] = [7, 8, 9]  # [7, 8, 9, 4, 5, 6]


#Delete multiple items at once
del a[:2]  # [3, 4, 5, 6]

#Resize a list by other items
a[:4] = [7, 8]  # [7, 8, 5, 6]


#Use the Slice Object To Store Indexes
a = [1, 2, 3, 4, 5, 6]
b = [3, 4, 5, 6, 7, 8, 9]
c = [2, 3, 4, 5, 100, 101, 102]

a2 = a[1:5:2]
b2 = b[1:5:2]
c2 = c[1:5:2]
