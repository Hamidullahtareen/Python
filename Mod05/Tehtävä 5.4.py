right_answer = 6

number = float(input("Guess the right number and win 1000€: "))

while number != right_answer:
    number = float(input("Try again: "))
    if number < right_answer:
        print("Bigger then this")
    if number > right_answer:
        print("Smaller then this")
print("Right answer and won 1000€")