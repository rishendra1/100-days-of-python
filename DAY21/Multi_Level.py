class Grandfather:
    text1 = "I am grandfather"
class Parent(Grandfather):
    text2 = "I am parent"
class Child(Parent):
    text3 = "I am child"
c1 = Child()
print(c1.text3)
print(c1.text2)
print(c1.text1)
