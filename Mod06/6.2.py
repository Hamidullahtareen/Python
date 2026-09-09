number = input("Enter a number: ")
number = float(number)
list = []

while number != "":
    number = float(number)
    number = input("Enter a number: ")
    list.append(number)
list.sort(reverse=True)
print("The greatest numbers in descending order: ")

for number in list[:5]:
    print(number)