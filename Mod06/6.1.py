import random

dice_roll = int(input("How many dice to roll: "))
total_of_dice = 0
for i in range(dice_roll):
    total_of_dice += random.randint(1,6)
print(f"Sum of the dice: {total_of_dice}")