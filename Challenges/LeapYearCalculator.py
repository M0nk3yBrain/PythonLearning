# Which year do you want to check?
year = int(input())
# Set 2 variables to reduce typing input
yLeap = 'Leap year'
nLeap = 'Not leap year'
# Year Check logic with three checks
if year % 4 == 0:
  if year % 100 == 0: #Not a leap year unless also cleanly diviable by 400
    if year % 400 == 0:
      print(yLeap)
    else:
      print(nLeap)
  else:
    print(yLeap)
else:
  print(nLeap)