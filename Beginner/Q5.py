num = input("Enter a number: ")
fact = 1
for i in range(1, int(num)+1):
    fact *= i
print("Factorial of", num, "is", fact)