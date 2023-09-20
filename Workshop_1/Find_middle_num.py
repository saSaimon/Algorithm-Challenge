def find_middle_num(x, y, z):
    if x>y and x<z:
        print(x)
    elif x<y and x>z:
        print(x)
    elif y>z and y<x:
        print(y)
    elif y<z and y>x:
        print(y)
    elif z>y and z<x:
        print(y)
    elif z<y and z>x:
        print(y)

find_middle_num(10, 6, 4)





