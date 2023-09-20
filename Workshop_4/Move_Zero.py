def move_zero(arr):
    for i in arr:
        if i==0:
            arr.remove(0)
            arr.append(0)
    print(arr)
list= [0 ,4, 0, 3, 12]
move_zero(list)