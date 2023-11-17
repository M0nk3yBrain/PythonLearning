# Input a Python list of student heights
# Input 151 145 179
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total = 0
number = 0
for heights in student_heights:
  total += heights
for height in student_heights:
  number +=1
average = round(total / number)
print(f"total height = {total}")
print(f"number of students = {number}")
print(f"average height = {average}")