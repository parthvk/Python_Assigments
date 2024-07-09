string1 = input("Enter a string: ")
string2 = input("Enter another string: ")
# check anagram
if sorted(string1) == sorted(string2):
    print("True")
else:    
    print("False")