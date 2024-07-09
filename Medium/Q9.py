# Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
def operation(list, index):
    try:
        return list[index]+1
    except IndexError:
        return "Index out of range"
    
print(operation([1,2,3], 3))