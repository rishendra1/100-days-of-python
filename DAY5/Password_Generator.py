#Password Generator
import random
Letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Numbers = ['1','2','3','4','5','6','7','8','9','0']
Characters = ['!','*','$','@']
n1 = int(input("Enter Number of letters do you want: "))
n2 = int(input("Enter Number of Numbers do you want: "))
n3 = int(input("Enter Number of characters do you want: "))
Final_Password = []
for char in range(1, n1 + 1):
    character = random.choice(Letters)
    Final_Password += character

for char in range(1, n2 + 1):
    character = random.choice(Numbers)
    Final_Password += character

for char in range(1, n3 + 1):
    character = random.choice(Characters)
    Final_Password += character
random.shuffle(Final_Password)
str(Final_Password)
Final_Password = "".join(Final_Password)
print(Final_Password)