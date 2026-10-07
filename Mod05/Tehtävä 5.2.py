
CM_PER_INCH = 2.54

while True:
    inches = float(input("Enter length in inches (negative value to quit): "))
    if inches < 0:
        break
    print(f"{inches} inches is {inches * CM_PER_INCH:.2f} centimeters")
print("Program ended.")