row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
full_map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
# first digit is column, second digit is row eg. 21 would be second column and 1st row
position = input("Where do you want to put the treasure? enter column position then row position ")

column = int(position[0]) - 1
row = int(position[1]) - 1

full_map[row][column] = "X"
print(f"{row1}\n{row2}\n{row3}")




