physics = input("Enter Physics marks out of 100:")
chemistry = input("Enter Chemistry marks out of 100:")
biology = input("Enter Biology marks out of 100:")
math = input("Enter Mathematics marks out of 100:")
computer = input("Enter Computer marks out of 100:")
percentage = (int(physics) + int(chemistry) + int(biology) + int(math) + int(computer)) / 5
if percentage >= 90:
    print("Grade A")
elif percentage >= 80:
    print("Grade B")
elif percentage >= 70: 
    print("Grade C")
elif percentage >= 60:
    print("Grade D")
elif percentage >= 40:
    print("Grade E")
else:
    print("Grade F")