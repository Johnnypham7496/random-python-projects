weight = float(input('Enter your weight in lbs: '))
height = float(input('Enter your height in inches: '))

bmi = weight / (height**2 ) * 703

print(f'Your body index is: {bmi:.2f}')

if bmi > 0: 
    if bmi <= 16:
        print('You are severly underwright')
    elif bmi <= 18.5:
        print('You are underweight')
    elif bmi <= 25:
        print('You are normal')
    elif bmi <= 30:
        print('You are overweight') 
    else:
        print('You are severely overweight')
else:
    print('Enter valid details')