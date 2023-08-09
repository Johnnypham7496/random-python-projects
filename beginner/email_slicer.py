# strip will remove all of the white space from the outside of the email
email = input("Enter your email: ").strip()
# everything after the colon in the square brackets will be inlcuded until the @ symbol
username = email[:email.index("@")]
# in this instance the index will be the number placement where the @ symbol. By adding +1 we skip the @ symbol and move the next placement
domain_name = email[email.index("@")+1:]
format_ = (f'Your username is {username} and your domain name is {domain_name}')
print(format_)