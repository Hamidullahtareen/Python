import random
def gallons_to_liters(galon):
    return galon * 3.785

galon = float(input("Enter a volume in American gallons (negative value to quit): "))
   


while galon >= 0:
    liter = gallons_to_liters(galon)
    print(f"{galon} American gallons is {liter:.2f} liters.")
    galon = float(input("Enter a volume in American gallons (negative value to quit): "))
print("Program finished.")
     