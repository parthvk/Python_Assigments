# 3. Aditi has used text editing software to type some text. After saving the article as words.txt, she realized that she had wrongly typed the alphabet “J" instead of “I" everywhere in the article. Write a function definition for JtoI() in Python that would display the corrected version of the entire content of the file WORDS.TXT with all the alphabet "J" to be displayed as an alphabet "I" on the screen. Note: Assume that words.txt does not contain any J alphabet otherwise.

def JtoI():
    f = open("words.txt", "r")
    lines = f.readlines()
    f.close()
    
    for line in lines:
        print(line.replace('J', 'I').strip('\n'))

JtoI()