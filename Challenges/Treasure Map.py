# Treasure Map
# My conviluted way.
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
forInput = position.lower()
row1 = "1"
row2 = "2"
row3 = "3"
columna = "a"
columnb = "b"
columnc = "c"

if row1 in forInput:
  if columna in forInput:
    line1[0] = "X"    
  elif columnb in forInput:
    line1[1] = "X"
  else:
    line1[2] = "X"
elif row2 in forInput:
  if columna in forInput:
    line2[0] = "X"    
  elif columnb in forInput:
    line2[1] = "X"
  else:
    line2[2] = "X"
else:
  if columna in forInput:
    line3[0] = "X"    
  elif columnb in forInput:
    line3[1] = "X"
  else:
    line3[2] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")