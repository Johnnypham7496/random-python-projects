# To create acronyms using Python, you need to write a python program that generates a short form of a word from a given sentence. 
# You can do this by splitting and indexing to get the first word and then combine it.

user_input = str(input("Enter a Phrase: "))
# strip will remove all of the white space from the outside of the email
text = user_input.split()

a = " "
# creating a loop for all of the words within the input text
for i in text: 
    a = a+str(i[0]).upper()

print(a)