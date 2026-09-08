#Tehtävä 3.3
base_str = input ("Mikä on suorakulmion kanna?")
height_str = input ("Mikä on suorakulmion korkeus?")

base = float(base_str)
height = float(height_str)

paramitter = 2 * base + 2 * height
print("Suorakulmion piiri on :" , + paramitter )

area = base * height
print("Suorankulmion pinta-ala on:" , + area)