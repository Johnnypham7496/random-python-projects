# a while loop to continue taking multiple inputs until stopped

while True:
    if (reply := input('Enter Text: ').lower()) == 'stop':
        break
    print(reply)
