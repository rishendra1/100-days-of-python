class Experience:
    @staticmethod
    def increment_calculator(value):
        increment = 0
        if 1 < value <= 3:
            increment = 1
        if 3 < value <= 5:
            increment = 3
        if value > 5:
            increment = 5
        return increment
class employee(Experience):
    def __init__(self, name, role, experience):
        self.name = name
        self.role = role
        self.experience = experience
        print(f"Name : {self.name}\nRole : {self.role}\nExperience : {self.experience}years")
Name = input("enter name: ")
Role = input("enter Role: ")
exp = int(input("enter experience: "))
Employee1 = employee(Name, Role, exp)
print(f"Congratulations!!! you earned increment of {Employee1.increment_calculator(exp)}% of your salary")