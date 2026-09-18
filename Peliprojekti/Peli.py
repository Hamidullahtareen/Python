
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
            print("Lets go to find the tressure together.")
            door = input("Chose the door you want to go: 'A'or 'B' or 'C': ")
            if door == "A":
                print("Eaten by liones")
                print("Start again")
            elif door == "B":
                print("Eaten by wolfes.")
                print("Start again")
            elif door == "C":
                print("No way back from here. Lets gooooo!")
                challeng = input("Are you ready to face the challenges? 'Y' or 'N': ")
                if challeng == "Y":
                    print("Then be STRONG")
                    print("Walk straight for 200m from here.")
                    print("Ohhhhh seems you have to chose for these three roads!!!")
                    path = input("Chose road A, road B or road C")
                    if path == "A":
                        print("You chose the Forest path.")
                        print("You walk deeper into the forest.\n After 100 meters, you see an old wooden sign.\n The sign says: Olny those who look carefully will find the way. ")
                        print("You chose the Forest path.")
                        
                    #here again need to put choice of 
                elif challeng == "N":
                    print("Seems that you are not that strong.")
        elif command == "quite":
            print("Good Bye")
        else:
           print("Unkown command")
        break


    
