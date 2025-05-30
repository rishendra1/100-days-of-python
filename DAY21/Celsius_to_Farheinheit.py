class convertion:
    def __init__(self, Temperature):
        self.Temperature = Temperature
    def convert_to_farheinheit(self):
        return (self.Temperature * 9 / 5) + 32
    def convert_to_celsius(self):
        return (self.Temperature - 32) * 5/9
while True:
    choice = input("Which operation do you select?\n(type - 'f'(fahreinheit to Celsius)) \n(type - 'c'(celsius to Farheinheit))\ntype - 'exit' to exit: ")
    if choice == 'f':
        Fahrenheit = int(input("Enter the temperature in Fahrenheit: "))
        c1 = convertion(Fahrenheit)
        convert = c1.convert_to_celsius()
        print(f"The temperature in Celsius is: {convert}")
    elif choice == 'c':
        Celsius = int(input("Enter the temperature in Celsius: "))
        c1 = convertion(Celsius)
        convert = c1.convert_to_farheinheit()
        print(f"The temperature in Celsius is: {convert}")
    elif choice == 'exit':
        break