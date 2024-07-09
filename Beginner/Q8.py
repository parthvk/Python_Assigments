num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
num1 = int(num1)
num2 = int(num2)
greater = max(num1, num2)
smaller = min(num1, num2)
for i in range(greater, (num1*num2)+1, greater):
    if i % smaller == 0:
        print("LCM of", num1, "and", num2, "are:", i)
        break