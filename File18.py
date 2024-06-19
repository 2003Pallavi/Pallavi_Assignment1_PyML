# Check if 2 strings are anagrams of each other

str1 = input("Enter a string: ")
rev_str = str1[::-1]
str2 = input("Enter another string(anagram): ")
if(str2==rev_str):
    print("The 2 strings",str1,"and",str2,"are anagrams")
else:
    print("The 2 strings",str1,"and",str2,"are NOT anagrams")