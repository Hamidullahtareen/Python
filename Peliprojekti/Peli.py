
name_str = input("What is you name ?")
age = int(input("What is your age ?"))
print(f"Your name is {name_str} and your age is {age}")

if age <= 12 :
    print("Sorry you can not play the game.")
else:
    print("Welcome to the Game")

    while True:
        print("\nMain Menu")
        print("1.play")
        print("2.Help")
        print("Type 'quit' to exit ")

        command = input("Enter your command: ")
        if command == "play":
            print("Lets go to find the tressure togither.")
            door = input("Chose the door you want to go: 'A'or 'B' or 'C': ")
            if door == "A":
                print("Eaten by liones")
                print("Start again")
            elif door == "B":
                print("Eaten by wolfes.")
                print("Start again")
            elif door == "C":
                print("Here is the map to tressure.")
                direction = input("Ready to be directed? 'Y' or 'N': ")
                if direction == "Y":
                    print("Lets gooooo.")
                    print("from here go right and strait 200m.")
                    #here again need to put choice of 
                elif direction == "N":
                    print("Seems you dont need help. Good luck finding tressure.")
        elif command == "quite":
            print("Good Bye")
        else:
           print("Unkown command")
        break


    
