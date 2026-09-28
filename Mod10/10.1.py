class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
        print(f"Elevator is now at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
        print(f"Elevator is now at floor {self.current_floor}")

    def go_to_floor(self, target):
        if target > self.top_floor or target < self.bottom_floor:
            print(f"Floor {target} is out of range ({self.bottom_floor}-{self.top_floor})")
            return

        while self.current_floor < target:
            self.floor_up()

        while self.current_floor > target:
            self.floor_down()