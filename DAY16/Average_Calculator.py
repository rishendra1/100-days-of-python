class Student:
    def __init__(self, name, maths, physics, chemistry):
        print("Adding Student details: ")
        self.name = name
        self.maths = maths
        self.physics = physics
        self.chemistry = chemistry
        self.avg = (self.maths +  self.physics + self.chemistry) / 3
        print(f"Name - {self.name}\nmaths - {self.maths}\nphysics - {self.physics}\nChemistry - {self.chemistry}\nAverage - {round(self.avg,2)}")
    def grade(self):
        Average = self.avg
        if 91 < Average < 100:
            print("Topper - 'O' grade")
        if 81 < Average < 90:
            print("You got - 'A+' grade")
        if 71 < Average < 80:
            print("You got - 'A' grade")
        if 61 < Average < 70:
            print("You got - 'B+' grade")
        if 51 < Average < 60:
            print("You got - 'B' grade")
        if 40 < Average < 50:
            print("You got - 'C' grade")
        if 30 < Average < 40:
            print("You got - 'D' grade")
        if 0 < Average < 30:
            print("You Failed")
Name = input("Enter Student Name: ")
Maths = int(input("Enter Maths marks: "))
Physics = int(input("Enter Physics marks: "))
Chemistry = int(input("Enter Chemistry marks: "))
s1 = Student(Name, Maths, Physics, Chemistry)
grade = s1.grade()