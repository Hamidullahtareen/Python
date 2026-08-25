

# Tehtävä 3.1
name = input ("Mikä on sinun nimesi?: ")
print ("Hei " + name + "! Mukava tavata sinut.")


# Tehtävä 3.2
radius_str= input ("Anna ympyrän säde: ")
radius = float(radius_str)        
area = 3.14 * radius ** 2
print(f"Ympyrän pinta-ala on: {area:.2f}")


#Tehtävä 3.3
base_str = input ("Mikä on suorakulmion kanna?")
height_str = input ("Mikä on suorakulmion korkeus?")

base = float(base_str)
height = float(height_str)

paramitter = 2 * base + 2 * height
print("Suorakulmion piiri on :" , + paramitter )

area = base * height
print("Suorankulmion pinta-ala on:" , + area)



#Tehtävä 3.4
number_one = input("Mikä on sinun ensimmäinen luku? ")
number_two = input("Mikä on sinun toinen luku? ")
number_three = input("Mikä on sinun kolmas luku? ")

namber_1 = float(number_one)
namber_2 = float(number_two)
namber_3 = float(number_three)

summa = namber_1 +namber_2 + namber_3
print("Sinun antama numeron summa on:" , summa)

tulon = namber_1 * namber_2 * namber_3
print("Sinun antama numeron tulo on:" , tulon)

keskiarov = summa / 2
print("Sinun antama numeron keskiarvo on:" , keskiarov)

#Tehtävä 3.5
question_levi = float(input("kuinka paljon painoa leiviskät on?"))
question_naulat = float(input("kuinka paljon painoa naulat on?"))
question_luodit = float(input("kuinka paljon painoa luodit on?"))
# tässä mä vaihtanut määrää kilogrammoiksi että lasketaan helposti.
levi = question_levi * 8.512
naulat = question_naulat * 0.4256
luodit = question_luodit * 0.0133

summa = levi + naulat + luodit
gramma = summa / 1000
print(f"Massa nykymuttojen mukaan: {summa:.1f} Killogramma ja {gramma:.4f} gramma")


#Tehtävä 3.6
import random

luku = random.randint(0,9)
luku2 = random.randint(0,9)
luku3 = random.randint(0,9)

print(f"{random.randint(0,9)} {random.randint(0,9)} {random.randint(0,9)}")

print(f"{random.randint(0,6)} {random.randint(0,6)} {random.randint(0,6)} {random.randint(0,6)}")

