# Convert F to C and vice versa
print('''1. Convert to Fahrenheit
2. Convert to Celsius''')

num1 = int(input("Enter the temperature: "))
ch = int(input("Enter choice(1 or 2)"))
res = 0
if (ch==1):
    res = (9/5)*num1 + 32
    print("The temperature in deg F is: ",res)
elif (ch==2):
    res = (num1-32)*(5/9)
    print("The temperature in deg c is: ", res)
else:
    print("INCORRECT CHOICE!!!!")