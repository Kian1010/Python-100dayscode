import art
import os
user_dict = []
print(art.logo)
done = 'yes'


def new_user(name,bid):
    user_dict.append({"name": name, "bid": bid},)


def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


while done != 'no':
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: R"))
    new_user(name, bid)
    done = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if done == 'yes':
        clear()

highest = 0
winner = ""
for users in user_dict:
    if users["bid"] > highest:
        highest = users["bid"]
        winner = users["name"]
print(f"The winner is {winner} with a bid of R{highest}")
