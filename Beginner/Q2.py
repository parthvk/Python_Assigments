s = input("Enter string:")
charcount = 0
digitcount = 0
for i in s:
    if i.isalpha():
        charcount += 1
    elif i.isdigit():
        digitcount += 1
print("Alphabets = ", charcount , " ,  Digits = " , digitcount)