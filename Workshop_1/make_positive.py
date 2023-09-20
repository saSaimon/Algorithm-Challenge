import math

def make_positive(number):
    if number < 0:
         positive_num = -(number)
         return positive_num
    else:
        return number
print(make_positive(-.3))
