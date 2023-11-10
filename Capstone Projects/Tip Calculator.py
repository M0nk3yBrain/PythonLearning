print('Welcome to the tip calculator.')
#What was the toatl bill? input()
bill = float(input('What was the toatl bill?\n$'))
#How many people to split the bill?input()
party = int(input('How many people to split the bill?\n'))
#What percentage tip would you like to give? 10, 12, or 15? input()
percent = int(input('What percentage tip would you like to give? 10, 12, or 15?\n'))
# Each person should pay: print()
tipTotal = bill * (percent / 100)
tip = (tipTotal + bill) / party
#Formats the tip to 2 decimal points
tip = "{:.2f}".format(tip)
print(f'Each person should pay: ${tip}')