#Write a Python program to create a list of given strings individually of the list using the Python map function.
def string_to_list(str):
    return list(str)

def strings_to_lists(lst):
    return list(map(string_to_list, lst))

input_list = ['Red', 'Blue', 'Black', 'White', 'Pink'] 
print(strings_to_lists(input_list))