user_name = input("Enter user name here: ").lower()
password = input("Enter password name here: ").lower()

while user_name != "python" or password != "rules":
    print("Access denid. Try again")
    user_name = input("Enter user name here: ")
    password = input("Enter password name here: ")
print("Access granted. Welcome to programme.")