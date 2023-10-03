# a while loop to continue taking multiple inputs until stopped

while True:
    reply = input('Enter Text: ').lower()
    if reply == 'stop':
        break
    print(reply)