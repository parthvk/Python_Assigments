#Write a Python function that counts the number of vowels in a given string.
def count_vowels(str):
    vowels = "aeiouAEIOU"
    count = 0
    for i in str:
        if i in vowels:
            count += 1
    return count

print(count_vowels("Hello, World!")) 