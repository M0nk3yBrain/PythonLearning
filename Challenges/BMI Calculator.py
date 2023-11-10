print('BMI Calculater using meters and kilograms')
# 1st input: enter height in meters e.g: 1.65
height = input('Enter height in meters: ')
# 2nd input: enter weight in kilograms e.g: 72
weight = input('Enter weight in kilograms: ')

weight = float(weight)
height = float (height)

bmi = round(weight / height ** 2)

print('Your BMI is:',bmi)