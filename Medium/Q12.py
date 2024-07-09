#Create a login page backend to ask users to enter the username and password. Make sure to ask for a Re-Type Password and if the password is incorrect give a chance to enter it again but it should not be more than 3 times.
username = input("Enter username: ")
password = input("Enter password: ")
retype = input("Re-type password: ")
count = 0
while password != retype:
    count += 1
    if count == 3:
        print("You have entered the wrong password 3 times.")
        break
    print("Password does not match. Please try again.")
    retype = input("Re-type password: ")