smallest = 0
largest = 0

while True:
    number = input("Give me the number: ")
    if number == "":
        break
    number = float(number)
    if smallest < number:
        smallest = number

    if largest > number:
        largest = number
print(f"the largest is {largest} and the smallest is {smallest}")