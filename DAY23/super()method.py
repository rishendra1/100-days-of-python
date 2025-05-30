class Car:
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("Car started........")
    @staticmethod
    def stop():
        print("Car stopped........")
class ToyotaCar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)
car1 = ToyotaCar("Toyota", "Petrol")
print(car1.type)
car1.start()
car1.stop()