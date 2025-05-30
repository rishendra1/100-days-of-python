class Car:
    @staticmethod
    def start():
        print("The car is now started.")
    @staticmethod
    def stop():
        print("The car is now stopped.")
class Maruthi_Suzuki(Car):
    def __init__(self, brand):
        self.brand = brand
class Celerio(Maruthi_Suzuki):
    def __init__(self, type, year):
        self.type = type
        self.year = year
Car1 = Celerio("Petrol", 2018)
Car1.start()