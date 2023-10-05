# shopping cart program


foods = []
prices = []
total = 0


while True:
    food = input('Enter a food to buy (q to quit): ')
    if food.lower() == 'q':
        break
    