#Create a function that takes a list and returns a new list with unique elements of the first list.
def uniqueElements(list1):
    set1 = set(list1)
    return list(set1)

list1 = [1, 2, 2, 3, 4, 4, 5, 5]
print(uniqueElements(list1))