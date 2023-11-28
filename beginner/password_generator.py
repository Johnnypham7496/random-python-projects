import secrets

# loop to make sure user is entering an integer and not a string character
# this generator does not exceed 74 characters
while True: 
    try:
        pass_len = int(input("Enter the length of your password here: "))
        break
    except ValueError:
        print('Invalid input. Please enter a integer')

s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
# this will take the users int input and randomly select characters and numbers from the 's' variable to generate a random password
p = "".join(secrets.SystemRandom().sample(s,pass_len))
print(p)
