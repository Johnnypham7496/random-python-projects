# example countdown timer

import time 


my_time = int(input('Enter the time in seconds: '))

# x is our counter that loops through numbers starting from 0 until it reaches my_time
# range(my_time, 0, -1) is a method we use to have the counter count numbers in reverse. Another method is using reverse()
# there is no 'days' field so we don't need '% 24' in our hours variable
for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
    

print('TIME\'S UP')