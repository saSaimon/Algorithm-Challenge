
def BinGo(num):
    if num%3==0 and num%7==0:
        print('BinGo')
    elif num%3==0:
        print('Bin')
    elif num%7==0:
        print('Go')
    else:
        print(num)
BinGo(21)