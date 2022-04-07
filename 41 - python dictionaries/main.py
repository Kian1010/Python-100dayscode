# A dictionary is created by assigning a variable with {} which contain key and value pairs
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

old_programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

# This code appends or adds to the dictionary
programming_dictionary["Loop"] = "Something that is repeated over and over again"

# If an item already exists in a list, the value gets changed
programming_dictionary["Bug"] = "A moth that has entered your computer"

# This is how to clear all the information within the dictionary, by declaring empty {}
old_programming_dictionary = {}

# This code adds onto the existing dictionary
programming_dictionary["Function"] += " Especially if the instructions are repeated often"

print(programming_dictionary)
print(old_programming_dictionary)

# This is how you would loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
