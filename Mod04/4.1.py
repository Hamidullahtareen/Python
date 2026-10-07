#Tehtävä 4.1

fish_size = float(input("Enter the length of the zander in centimeters: "))
fish = 42 
missing = 42 - fish_size 


if fish_size < fish:
    print("The zander does not meet the size limit.")
    print("Please release the fish back into the lake.")
    print(f"The fish was {missing:.1f} centimeters below the size limit.")
else:
    print("The zander meets the size limit.")





 
