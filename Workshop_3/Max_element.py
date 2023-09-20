def max_element(arr):
    # sorted_list = sorted(arr)
    # print(sorted_list)
    #
    # increasing_order = (sorted_list[::-1])
    # print(increasing_order[0])

    max_num = max(arr)
    print(max_num)
    peak_index = arr.index(max(arr))
    print(peak_index)

list = [2,3,5,2,5,4,0]
max_element(list)