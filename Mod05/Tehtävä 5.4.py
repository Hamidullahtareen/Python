# import random
# right_answer = random.randint(1,10)

# # number = float(input("Guess a number (1-10): "))

# while number != right_answer:
#     number = float(input("Guess a number (1-10): "))
#     if number < right_answer:
#         print("Too high")
#     if number > right_answer:
#         print("Too low")
# print("Correct")


import random

secret = random.randint(1, 10)

while True:
    guess = int(input("Guess the number (1-10): "))

    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print("Correct")
        break