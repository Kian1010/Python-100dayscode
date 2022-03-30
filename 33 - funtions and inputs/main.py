# # Review:
# # Create a function called greet().
# def greet():
#     print("hi")
#     print("hii")
#     print("hiii")
#
#
# # Write 3 print statements inside the function.
# # Call the greet() function and run your code.
#
# greet()
#
#
# def name_greet(name):
#     print(f"Hi there {name}")
#
#
# name_greet(input("type your name:\n"))

# functions with more than 1 input (positional argument)

# def greet_with(name, location):
#     print(f"Hi {name}, you are currently in {location}")
#
#
# greet_with("Kian", "South Africa")

# functions with keyword arguments

def greet_with(name, location):
    print(f"Hi {name}, you are currently in {location}")


greet_with(location="South Africa", name="kian")
