#Write a Python program to reverse a number using a while loop.
def reverse(num):
    rev = 0
    while num > 0:
        rev = rev*10
        rev = rev + num%10
        num = num//10
    return rev

num = 12345
print(reverse(num))