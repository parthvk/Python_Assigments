#Given an input string, write a function that returns the run length encoded string for the input string.

def rle(input):
    curr_char = input[0]
    count = 1
    result = ""
    for i in range(1, len(input)):
        if input[i] == curr_char:
            count += 1
        else:
            result += curr_char + str(count)
            curr_char = input[i]
            count = 1
    result += curr_char + str(count)
    return result

input = "wwwwaaadebbbbbw"
print(rle(input))