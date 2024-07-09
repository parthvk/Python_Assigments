#Write a program to count the lines in a file “demo.txt” 

f = open("doc.txt", "r")
lines = f.readlines()
f.close()
print(len(lines))