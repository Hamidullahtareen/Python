
attempts = 0

while attempts < 5:
    username = input("Enter username: ").lower()
    password = input("Enter password: ").lower()

    if username == "python" and password == "rules":
        print("Welcome")
        break

    attempts += 1
    if attempts < 5:
        print("Incorrect username or password. Please try again.")
else:
    print("Access denied")