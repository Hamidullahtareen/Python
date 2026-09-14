def get_season(month):
    if month == 12 or month == 1 or month == 2:
        return "winter"
    elif month == 3 or month == 4 or month == 5:
        return "spring"
    elif month == 6 or month == 7 or month == 8:
        return "summer"
    elif month == 9 or month == 10 or month == 11:
        return "autumn"

month = int(input("Enter the number of a month (1-12): "))

if month >= 1  and month <= 12:
    print(f"You entered: {month}\nThe season is {get_season(month)}.")
else:
    print(f"You entered: {month}\nPlease enter a number between 1 and 12.")