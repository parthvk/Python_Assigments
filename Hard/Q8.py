#8. You need to write a function that accepts an encoded string as a parameter. This string will contain a first name, last name, and an id. Values in the string can be separated by any number of zeros. The id is a numeric value but will contain no zeros. The function should parse the string and return a Python dictionary that contains the first name, last name, and id values.

def parse_string(encoded_string):
    arr = []
    temp = ""
    for i in range(len(encoded_string)):
        if encoded_string[i] == "0":
            if temp != "":
                arr.append(temp)
                temp = ""
        else:
            temp += encoded_string[i]

    if temp != "":
        arr.append(temp)

    return {"first_name": arr[0], "last_name": arr[1], "id": int(arr[2])}

encoded_string =  "Robert000Smith000123"
print(parse_string(encoded_string))