class Car:
    current_speed = 0
    travelled_distance = 0

    def __init__(self, license_plate, maximum_speed, current_speed, travelled_distance):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed

        
    car1 = Car("ABC-123","142 km/h", 0, 0)
    print(f"License plate: {car1.license_plate}\nMaximum speed: {car1.maximum_speed}\nCurrent speed: {car1.current_speed} km/h\nTravelled distance: {car1.travelled_distance} km")
