import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

result = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
#  0 > 2 ; 0 < 1
# 1 > 0 ; 1 < 2
#  2 > 1 ; 2 < 0
#
#
#
machine_choice = random.randint(0, 2)

if result == 0:
    print(rock)
elif result == 1:
    print(paper)
elif result == 2:
    print(scissors)

print("Machine chose:\n")

if machine_choice == 0:
    print(rock)
elif machine_choice == 1:
    print(paper)
elif machine_choice == 2:
    print(scissors)

if result == machine_choice:
    print("It's a draw")
elif result == 0 and machine_choice == 2:
    print("You win")
elif result == 1 and machine_choice == 0:
    print("You win")
elif result == 2 and machine_choice == 1:
    print("You win")
else:
    print("You lose")
