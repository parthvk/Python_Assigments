#Write a Python program to find the common elements between two lists.
def commonElements(list1, list2):
    list3 = []
    dict1 = {}
    for i in list1:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    
    for i in list2:
        if i in  dict1:
            list3.append(i)
            dict1[i] -= 1
            if dict1[i] == 0:
                dict1.pop(i)
    return list3

l1 = [1, 1, 2, 3, 4, 5] 
l2 = [1, 1, 4, 5, 6, 7, 8]
print(commonElements(l1, l2))