num = input("Enter a number: ")
div = 0
for i in range(1, int(num)):
    if int(num) % i == 0:
        div += i
if div == int(num):
    print("Yes")
else:
    print("No")