import random


class Car:
    def __init__(self, license_plate, maximum_speed):
        self.registration_number = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        print(f"Race: {self.name} ({self.distance} km)")
        print(f"{'Registration':<15}{'Max speed':>12}{'Speed':>10}{'Distance':>12}")
        print("-" * 49)
        for car in self.cars:
            print(f"{car.license_plate:<15}"
                  f"{car.maximum_speed:>9} km/h"
                  f"{car.current_speed:>7} km/h"
                  f"{car.travelled_distance:>9} km")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False