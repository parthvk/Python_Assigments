#Write a Python function that finds the median of a list of numbers.
def median(list):
    list = sorted(list)
    n = len(list)
    if n%2 == 0:
        return (list[(n-1)//2] + list[n//2])/2
    return list[n//2]
list = [7, 2, 5, 1, 9, 3]
print(median(list)) 