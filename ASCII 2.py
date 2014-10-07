#Max Louis
#ASCII 2
#04/10/14
import random

length = int(input("Enter the password length."))

for length in range(length):
    #Generating the symbols.
    generateLetter = random.randrange(97,122)
    generateCase = random.randrange(0,3)
    number = random.randrange(0,9)
    #ASCII conversion.
    character = chr(generateLetter)
    #This need to come after conversion.
    symbol = random.randrange(0,2)
    #Outputs and determining which symbol to print.
    if symbol == 1 and generateCase == 2:
        print(character, end = "")
    elif symbol == 1 and generateCase == 1:
        character.upper()
        print(character, end = "")
    elif symbol == 2 and generateCase == 2:
        print(character, end = "")
    else:
        character.upper()
        print(number, end = "")


