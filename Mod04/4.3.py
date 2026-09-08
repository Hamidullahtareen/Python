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