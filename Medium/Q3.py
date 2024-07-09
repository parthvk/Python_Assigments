# Given an array of N integers and an integer K, find the number of pairs of elements in the array whose sum is equal to K.
def twoSum(arr, k):
    sumOfPairs = 0
    dict = {}
    for i in arr:
        if k-i in dict:
            sumOfPairs += dict[k-i]
        if i-k in dict:
            sumOfPairs += dict[i-k]
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return sumOfPairs

arr = [1,1, 2, 3, 4, 5] 
k = 6
print(twoSum(arr, k))