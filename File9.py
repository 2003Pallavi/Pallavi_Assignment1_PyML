# Checks if a substring is present in a given string

str1 = input("Enter a string: ")
sub_str = input("Enter the substring to be searched: ")
if(sub_str in str1):
    print("The substring",sub_str,"is present in the given string")
else:
    print("The substring was not found!!!")
