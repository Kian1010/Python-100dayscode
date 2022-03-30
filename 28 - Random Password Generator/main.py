# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

rletters = ""
rSymbols = ""
rNumbers = ""
lenLetters = len(letters)
lenSymbols = len(symbols)
lenNumbers = len(numbers)

# These 3 for loops gets the random amount of each desired letter,number and symbol randomly from the lists above
for iletter in range(1, nr_letters+1):
    rletters += letters[random.randrange(0, lenLetters)]

for isymbol in range(1, nr_symbols+1):
    rSymbols += symbols[random.randrange(0, lenSymbols)]

for inumber in range(1, nr_numbers+1):
    rNumbers += numbers[random.randrange(0, lenNumbers)]

randomString = rletters+rSymbols+rNumbers
lenRandomString = len(randomString)
finalPassword = ""
print(randomString)

# First for loop iterates through the length of the randomString which has the unjumbled password.
# finalPassword gets random values from the unjumbled password in order to mix the numbers, letters and symbols randomly
for randomChar in range(0, lenRandomString):
    value = random.randrange(0, len(randomString))
    finalPassword += randomString[value]
    temp = ""

# This for loop removes the value that was randomly chosen from randomString so that it is not chosen again when
# the random function extracts the next random character, the randomString variable is updated to its new value using
# a temp variable.
    for i in range(0, len(randomString)):
        if i != value:
            temp += randomString[i]
    randomString = temp

print(f"Your password is: {finalPassword}")
