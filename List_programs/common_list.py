""" Write a python program to take two list of integers and return a list containing the elements 
that are common in both the list. Also print the contents of new list."""
List1= []
limit = int(input("Enter the limit for both list:"))
for i in range(limit):
     num = int(input("Enter a number for the first list:"))
     List1.append(num)
print('List 1: ',List1)

List2= []
for i in range(limit):
     num = int(input("Enter a number for the second list:"))
     List2.append(num)
print('List 2: ',List2)

commonList = []
for n in List1:
    if n in List2:
        commonList.append(n)
print("Elements common in both lists:",commonList)