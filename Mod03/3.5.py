#Tehtävä 3.5
talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))
lot = lots * 13.3
pound = pounds * 32 * 13.3
talent = talents * 20 * 13.3 * 32
total_grams = lot + pound + talent 
kilograms = total_grams // 1000
remaining_grams = total_grams % 1000
print(f"The weight in modern units:{kilograms:.0f} kilograms and {remaining_grams:.2f} grams.")