def encoding(word):
    length = len(word)
    n = int(input("Enter number :"))
    b = [ord(char) for char in word]
    for i in range(0 , length):
        b[i] += n
    return b
def decoding(word):
    n = int(input("Enter number :"))
    length = len(word)
    b = [ord(char) for char in word]
    for i in range(0 , length):
        b[i] -= n
    return b

word = input("Enter a string: ")
q = input("Enter 'decode' to decode a number and 'encode' to encode a number : ")

if q == "decode":
   c = decoding(word)
if q == "encode":
    c = encoding(word)
d = ""
for i in range(len(c)):
    d += chr(c[i])
print(d)