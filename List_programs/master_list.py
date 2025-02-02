""" Write a python program to take a list of integers.Create another list with those numbers in the master list 
that are less than a number entered by the user. Print the new list contents."""
masterList= []
while True:
    num = int(input("Enter a number for the list :"))
    masterList.append(num)
    ch = input("Do you want to continue (y/n):")
    if ch!= 'y':
        break
print('Master List',masterList)
newList = []
num1 = int(input('Enter a number to filter:'))
for item in masterList:
    if(item <num1):
        newList.append(item)

print('New List is',newList)