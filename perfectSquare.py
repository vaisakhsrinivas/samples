'''
Given an integer, determine if it is a perfect square.

A number is a perfect square if you can multiply an integer by itself to achieve the number.
For example, 9 is a perfect square because you can multiply 3 by itself to get it.
'''



def perfect_square(n):

    low = 0
    high = n

    if n < 0:
        return False

    while low <= high:
        m = (low+high)//2
        if m*m == n :
            return True
        elif m*m < n :
            low = m + 1
        else:
            high = m - 1
    return False


print(perfect_square(9)) #should return True.
print(perfect_square(49)) #should return True.
print(perfect_square(1)) #should return True.
print(perfect_square(2)) #should return False.
print(perfect_square(99)) #should return False.
print(perfect_square(-9)) #should return False.
print(perfect_square(0)) #should return True.
print(perfect_square(25281)) #should return True.