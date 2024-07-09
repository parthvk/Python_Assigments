#Write a Python program to calculate the sum of digits of a given number until the sum becomes a single-digit number
def sumOfDigits(num):
    while num > 9:
        sum = 0
        while num > 0:
            sum += num % 10
            num = num//10
        num = sum
    return num

num = 987
print(sumOfDigits(num))