request_fahrenheit = input('Enter the temperature in fahrenheit: ')

def convert(s):
    f = float(s)
    c = (f - 32) * 5/9
    return c

print(f'The termperature from fahrenheit to celsius is {convert(request_fahrenheit):.2f}')