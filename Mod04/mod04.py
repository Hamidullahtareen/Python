
#Tehtävä 4.1

fish_size = int(input("What is the size of the fish in cm?"))
fish = 42 

if fish_size >= fish:
    print(f"The fish is {fish_size}cm and met the requirement, keep it!")
else:
    print(f"The fish is {fish - fish_size}cm below the requirement. Release the fish back lake") 



#Tehtävä 4.2
cabin_class = input("Please enter your cabin class:") 
cabin = "LUX" , "A" , "B" , "C"

if cabin_class == "LUX":
    print("Upper-deck cabin with a balcony.") 
elif cabin_class == "A":
    print("Above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("Windowless cabin above the car deck.")
elif cabin_class == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")  


#Tehtävä 4.3

gender = input("Please enter your gender:")
hemoglobin = float(input("Enter the your hemoglobin m/l:"))

if gender == "female":
    if hemoglobin < 117:
        print("Your hemoglobin level is Low")
    elif hemoglobin > 155:
        print("Your hemoglobin level is High")
    else:
        print("Your hemoglobin level is normal.")

if gender == "male":
    if hemoglobin < 134:
        print("Your hemoglobin level is Low")
    elif hemoglobin > 167:
        print("Your hemoglobin level is High")
    else:
        print("Your hemoglobin level is normal.")

 
#Tehtävä 4.4

year = int(input("Please enter the year here:"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.") 
