# converting roman numbers to decimal

# Python program to convert Roman Numerals
# to Numbers
 
# This function returns value of each Roman symbol
def value(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return -1
 
 
def roman_to_decimal(str):
    res = 0
    i = 0
 
    while (i < len(str)):
 
        # Getting value of symbol s[i]
        s1 = value(str[i])
 
        if (i + 1 < len(str)):
 
            # Getting value of symbol s[i + 1]
            s2 = value(str[i + 1])
 
            # Comparing both values
            if (s1 >= s2):
 
                # Value of current symbol is greater
                # or equal to the next symbol
                res = res + s1
                i = i + 1
            else:
 
                # Value of current symbol is greater
                # or equal to the next symbol
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1
 
    return res
 
 
# Driver code
# original code below
# print("Integer form of Roman Numeral is"),
# print(roman_to_decimal("MCMIV"))


# created while loop to continue to take in inputs of roman numerals until stopped
while True:
    request_roman_numerals = input('Enter a Roman numeral to be converted to a number. Enter "stop" to end: ')
    roman_number = roman_to_decimal(request_roman_numerals)

    if request_roman_numerals.lower() == 'stop':
        print('The progam has ended')
        break
    else:
        print(f"Integer form of Roman Numeral is {roman_number}")
