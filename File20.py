# take list of numbers and return their sum

lst1 = []
num1 = int(input("Enter the number of elements in list: "))
for i in range(0,num1):
    element = int(input("Number: "))
    lst1.append(element)
print("The list is: ",lst1)

sum = 0
for a in range(0,num1):
    sum = sum + lst1[a]
print("The sum of the elements is: ",sum)