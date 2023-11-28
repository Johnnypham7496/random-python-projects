import secrets

when = ['A few years ago', 'Yesterday', 'Last Night', 'A Long time ago', 'On 20th Jan']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle', 'a cat']
name = ['Ali', 'Miriam', 'Daniel', 'Johnny', 'Jason', 'Justin', 'Kristina', 'Skywalker']
residence = ['Gotham', 'New York', 'Metropolis', 'Pheonix', 'LA', 'San Francisco', 'Barcelona', 'Venice', 'England']
went = ['cinema', 'university', 'school', 'museum', 'laundry', 'basketball game', 'shopping']
happened = ['made a lot of friends', 'eats a burger', 'found a secret key', 'wrote a book', 'wwatched a movie', 'took photos']

print(secrets.SystemRandom().choice(when) + ', ' + secrets.SystemRandom().choice(who) + ' that lived in ' + secrets.SystemRandom().choice(residence) + ', went to the ' + secrets.SystemRandom().choice(went) + ' and ' + secrets.SystemRandom().choice(happened))
print(f'There was a {secrets.SystemRandom().choice(who)} that was from {secrets.SystemRandom().choice(residence)}, who went to {secrets.SystemRandom().choice(went)} and {secrets.SystemRandom().choice(happened)}')
