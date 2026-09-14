user_names = input("Please enter the name here: ")
names = set()
while user_names != "":
    if user_names in names:
        print("Existing name")
    else:
        print("New name")
        names.add(user_names)

    user_names = input("Please enter the name here: ")
print(names)