#Write a Python program to reverse the order of words in a given sentence
def reverseTheOrder(sentence):
    list = sentence.split()
    list.reverse()
    return " ".join(list)

sentence = "Hello, World! Welcome to Python programming."
print(reverseTheOrder(sentence))