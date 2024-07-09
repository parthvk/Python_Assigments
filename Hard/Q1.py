# .Read the doc.txt file using Python File handling concept and return only the even length string from the file. Consider the content of doc.txt as given below: Hello I am a file Where you need to return the data string which is of even length. Make sure you return the content in The same link as it is present.

f = open("doc.txt", "r")
lines = f.readlines()
f.close()

for line in lines:
        if len(line.strip('\n')) % 2 == 0:
            print(line.strip('\n'))
