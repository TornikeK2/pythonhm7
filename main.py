from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass


class Car(Vehicle):
    def __init__(self, max_speed):
        self.max_speed = max_speed
        self.current_speed = 0

    def start_engine(self):
        return "car started"

    def stop_engine(self):
        self.current_speed = 0
        return "car stopped"


class SportCar(Car):
    def start_engine(self):
        parent_result = super().start_engine()
        return f"{parent_result}, max speed: {self.max_speed}"

    def stop_engine(self):
        parent_result = super().stop_engine()
        return f"{parent_result}, current speed: {self.current_speed}"



car = SportCar(max_speed=200)
print(car.start_engine())  # Output: "car started, max speed: 200"
car.current_speed = 150
print(car.stop_engine())  # Output: "car stopped, current speed: 0"
