# Calculate sum of digits of an entered number

num1 = int(input("Enter the integer number: "))
var = num1
sum=0
while(var>=1):
    remainder = var%10
    sum = sum + remainder
    var = var//10

print("The sum of the digits of",num1,"is ",sum)
