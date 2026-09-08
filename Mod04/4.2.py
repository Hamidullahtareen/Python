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