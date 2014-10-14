#Max Louis
#ASCII 1
#3/10/14

ASCII = int(input("Input a 7 bit ASCII code."))

char = input("Input a character/symbol.")

print("Your code {0} is the same as:".format(ASCII))
ASCIIChar = chr(ASCII)
print(ASCIIChar)

print("Your character {0} is the same as:".format(char))
charASCII = ord(char)
print(charASCII)
