""" Write a python program to take a list of integers. Create another list to store all the even
numbers from the master list and print the new list contents in ascending order """
masterList= []
while True:
    num = int(input("Enter a number for the list:"))
    masterList.append(num)
    ch = input("Do you want to continue (y/n):")
    if ch!= 'y':
        break
print('Master List',masterList)
newList =list(filter(lambda n:n%2 == 0,masterList))
newList.sort()
print('New List with even integers:',newList)