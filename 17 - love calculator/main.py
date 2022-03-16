# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
#
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
#
# Then check for the number of times the letters in the word LOVE occurs.
#
# Then combine these numbers to make a 2 digit number.

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()

total1 = 0
total2 = 0

total1 += name1.count("t") + name2.count("t")
total1 += name1.count("r") + name2.count("r")
total1 += name1.count("u") + name2.count("u")
total1 += name1.count("e") + name2.count("e")

total2 += name1.count("l") + name2.count("l")
total2 += name1.count("o") + name2.count("o")
total2 += name1.count("v") + name2.count("v")
total2 += name1.count("e") + name2.count("e")

score = str(total1) + str(total2)

score = int(score)

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score <= 50) and (score >= 40):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")
