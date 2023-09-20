def two_lowest_element(arr):

    first_lowest_element = min(arr)
    arr.remove(first_lowest_element)
    list_2 = arr
    second_lowest_element = min(list_2)
    print(f'{first_lowest_element}, {second_lowest_element}')


list =  [198, 3, 4, 9, 10, 9, 2]

two_lowest_element(list)