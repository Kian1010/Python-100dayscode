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

rList = []
lenLetters = len(letters)
lenSymbols = len(symbols)
lenNumbers = len(numbers)

for iletter in range(1, nr_letters+1):
    rList += random.choice(letters)

for isymbol in range(1, nr_symbols+1):
    rList += random.choice(symbols)

for inumber in range(1, nr_numbers+1):
    rList += random.choice(numbers)

# This shuffles the list to a random order
random.shuffle(rList)

password = ""
for char in range(0, len(rList)):
    password += rList[char]

print(f"Your password is: {password}")
