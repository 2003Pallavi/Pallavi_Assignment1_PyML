#Check prefix and suffix of a given string

str1 = input("Enter a string: ")
prefix = input("Enter the prefix to be searched: ")
suffix = input("Enter the subscript to be seached: ")
if (str1[0]==prefix):
    print("The string has the prefix")
else:
    print("The string does not have the prefix")
if (str1[-1]==suffix):
    print("The string has the suffix")
else:
    print("The string does not have the prefix")