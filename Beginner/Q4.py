start = input("Enter the starting number:")
end = input("Enter the ending number:")
sum = 0
for i in range(int(start), int(end)+1):
    if i % 2 == 1:
        sum += i
print("Sum of odd numbers:", sum)