import math


def paint_calc(height, width, cover):
    num_cans = height * width / 5
    num_cans = math.ceil(num_cans)
    return num_cans


# Define a function called paint_calc() so that the code below works.

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
cans = paint_calc(height=test_h, width=test_w, cover=coverage)

print(f"You'll need {cans} cans of paint.")