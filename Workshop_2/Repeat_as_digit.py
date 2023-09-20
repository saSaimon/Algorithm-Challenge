def repeat_as_digit(n):
    list = []
    final_value = ''
    n = str(n)
    for i in n:
        list.append(i)
    for i in list:
        list_value = int(i)

        for j in range(list_value):
            final_value+=i
    print( final_value)
repeat_as_digit(123)