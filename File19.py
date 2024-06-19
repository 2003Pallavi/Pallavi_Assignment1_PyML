#program to remove all punctuations

str1 = input("Enter string: ")
str2 = ""
lst1= []
for a in range(0,len(str1)):
    if (str1[a]!=" ") and (str1[a]!=".") and (str1[a]!="?") and (str1[a]!="!") and (str1[a]!=",") and (str1[a]!=":"):
        lst1.append(str1[a])
print("The string without punctuation is ",str2.join(lst1))