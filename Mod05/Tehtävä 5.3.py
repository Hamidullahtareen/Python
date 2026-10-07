# smallest = 0
# largest = 0

# while True:
#     number = input("Enter a number (or press Enter to quit): ")
#     if number == "":
#         break
#     number = float(number)
#     if smallest < number:
#         smallest = number

#     if largest > number:
#         largest = number
# print(f"the largest is {largest} and the smallest is {smallest}")


smallest = None
largest = None

while True:
    entry = input("Enter a number (empty to quit): ")

    if entry == " ":
        break

    number = float(entry)

    if smallest is None or number < smallest:
        smallest = number
    if largest is None or number > largest:
        largest = number

if smallest is None:
    print("No numbers were entered.")
else:
    print(f"Smallest: {smallest}")
    print(f"Largest: {largest}")