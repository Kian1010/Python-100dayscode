# fruits = ["apple", "banana", "orange", "peach"]
#
# for x in fruits:
#     print(x)
#

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total = 0
count = 0

for i in student_heights:
    total += i
    count += 1

total = round(total / count)

print(total)
