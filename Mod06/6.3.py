number = int(input("Enter an integer: "))

prime = True

for i in range(2, number):
    if number % i == 0:
        prime = False

if number > 1 and prime:
    print("The number is a prime number.")
else:
    print("The number is not a prime number.")