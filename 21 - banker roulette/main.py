import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

name_length = len(names)

random_name = random.randint(0, name_length-1)

print(names[random_name] + " is going to buy the meal today!")
