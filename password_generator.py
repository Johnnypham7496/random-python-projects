import random
# prompting user to input length of a password in an integer format
pass_len = int(input("Enter the length of your password here: "))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
# this will take the users int input and randomly select characters and numbers from the 's' variable to generate a random password
p = "".join(random.sample(s,pass_len))
print(p)