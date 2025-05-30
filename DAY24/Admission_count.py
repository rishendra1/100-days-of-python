class Student:
    studentCount = 0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Student.studentCount += 1

    @classmethod
    def displayCount(cls):
        return cls.studentCount
s1 = Student("Rishendra",22)
s2 = Student("Thalapathy", 53)
s3 = Student("Vijay", 50)
print(Student.displayCount())