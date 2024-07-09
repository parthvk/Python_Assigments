#Write a program to construct a dictionary from the two lists containing the names of students and their corresponding subjects. The dictionary should map the students with their respective subjects. Let’s see how to do this using for loops and dictionary comprehension.
def construct_dict(students, subjects):
    dict = {}
    for i in range(len(students)):
        dict[students[i]] = subjects[i]
    return dict

students =  ["Sam", "Alice", "Mona"]
subjects = ["Commerce", "Science", "Computer"]
print(construct_dict(students, subjects))