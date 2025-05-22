# conversion of character string into a string of ascii values

a = "abcde"
b = [ord(char) for char in a]
print(b)