#Given an array of size N. The task is to rotate array by D elements towards right
def rotate(arr, d):
    d = d % len(arr)
    arr1 = []
    for i in range(len(arr)-d, len(arr)):
        arr1.append(arr[i])
    for i in range(len(arr)-d):
        arr1.append(arr[i])
    return arr1
arr = [1,2,3,4,5]
d = 2
print(rotate(arr, d))
