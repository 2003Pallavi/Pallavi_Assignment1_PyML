#Factorial of a number
def fact(a):
    res = 1
    for i in range(1,a+1):
        res = res*i
    return res

num1 = int(input("Enter the number: "))
fact = fact(num1)
print("The factorial of ",num1,"is ",fact)
