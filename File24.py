# Calculator
def sum(a,b):
    add = a+b
    print(add)
def subs(a,b):
    sub = a-b
    print(sub)
def mul(a,b):
    multi = a*b
    print(multi)
def div(a,b):
    divide = a/b
    print(divide)
print('''1. Addition
2.Subtraction
3.Multiplication
4.Division
5.EXIT''')
a=1
while (a):
    num1 = float(input("Enter 1st number: "))
    num2 = float(input("Enter 2nd number: "))
    ch = int(input("Enter your choice: "))
    if (ch==1):
        print("The sum of ",num1,"and ",num2,"is : ",sum(num1,num2))
    elif (ch==2):
        print("The subtraction of ", num1, "and ", num2, "is : ", subs(num1, num2))
    elif (ch==3):
        print("The multiplication of ", num1, "and ", num2, "is : ", mul(num1, num2))
    elif (ch==4):
        print("The division of ", num1, "and ", num2, "is : ", div(num1, num2))
    elif (ch==5):
        print("Exiting!!!!")
        a=0
    else:
        print("INCORRECT CHOICE!!!")
