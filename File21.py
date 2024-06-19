# Occurances of a specific element in list

lst1 = []
ele = int(input("Enter the number of elements: "))
for a in range(0,ele):
    element = int(input("Enter the list element: "))
    lst1.append(element)
print("The list is: ",lst1)
num1 = int(input("Enter the element to be searched: "))
count = 0
for i in range(0,ele):
    if (lst1[i]==num1):
        count = count +1
if (count!=0):
    print("The occurance of ",num1,"is: ",count)
else:
    print("Element not found in list")