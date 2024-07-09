#Write a Python program to find if a given string starts with a given character using Lambda
input_string = "Hello, World!"
given_char = "H"
result = lambda x,y : True if x.startswith(y) else False
print(result(input_string,given_char))