year = int(input("Which year do you want to check? "))

isLeap = False

if year % 4 == 0:
    isLeap = True
if year % 100 == 0:
    isLeap = False
if year % 400 == 0:
    isLeap = True

if isLeap:
    print("Leap year.")
else:
    print("Not leap year.")
