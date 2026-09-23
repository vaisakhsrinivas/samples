'''
Given two strings, determine if the second string is a mirror of the first.

A string is considered a mirror if it contains the same letters in reverse order.
Treat uppercase and lowercase letters as distinct.
Ignore all non-alphabetical characters.
'''


def is_mirror(str1, str2):

    stk1 = [ch for ch in str1 if ch.isalpha()]
    stk2 = [ch for ch in str2 if ch.isalpha()]

    if len(stk1) != len(stk2):
        return False

    for ch in stk2:
        if not stk1 or stk1.pop() != ch:
            return False
    return True


print(is_mirror("helloworld", "helloworld")) #should return False.
print(is_mirror("Hello World", "dlroW olleH")) #should return True.
print(is_mirror("RaceCar", "raCecaR")) #should return True.
print(is_mirror("RaceCar", "RaceCar")) #should return False.
print(is_mirror("Mirror", "rorrim")) #should return False.
print(is_mirror("Hello World", "dlroW-olleH")) #should return True.
print(is_mirror("Hello World", "!dlroW !olleH")) #should return True