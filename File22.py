# Return maximum and minimum numbers in a list

lst1 = []
elements = int(input("Enter the number of elements: "))
for i in range(0,elements):
    num1 = int(input("Enter number: "))
    lst1.append(num1)

print("The list is: ",lst1)
print("The max number in the list is: ",max(lst1))
print("The min number in the list is: ",min(lst1))