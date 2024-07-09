# Write a Python program to count the frequency of each element in a list
def countTheFreq(list):
    dict = {}
    for i in list:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

list = [1, 2, 3, 4, 1, 2, 3, 1, 2, 1]
print(countTheFreq(list))