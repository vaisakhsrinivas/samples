'''
Given a string, return "digits" if the string has more digits than letters, "letters" if it has more letters than digits, and "tie" if it has the same amount of digits and letters.

Digits consist of 0-9.
Letters consist of a-z in upper or lower case.
Ignore any other characters.
'''


import string


def digits_or_letters(s):
    digits = list("0123456789")
    alphabets = list(string.ascii_letters)

    digs = sum(1 for c in s if c in digits)
    alphas = sum(1 for c in s if c in alphabets)

    if digs > alphas:
        return "digits"
    elif alphas > digs:
        return "letters"
    else:
        return "tie"


print(digits_or_letters("abc123")) #should return "tie".
print(digits_or_letters("a1b2c3d")) #should return "letters".
print(digits_or_letters("1a2b3c4")) #should return "digits".
print(digits_or_letters("abc123!@#DEF")) #should return "letters".
print(digits_or_letters("H3110 W0R1D")) #should return "digits".
print(digits_or_letters("P455W0RD")) #should return "tie"