def min_element_and_subtract(arr):
    # sorted_list = sorted(arr, reverse=True)
    # # print(sorted_list)
    # min_num = min(arr)
    # output = []
    # for i in sorted_list:
    #     output.append(i-min_num)
    # print(output)]

    min_num = min(arr)
    output = []
    for i in arr:
      output.append(i-min_num)
    print(output)
list = [9, 2, 5, 4, 7, 6, 1]
min_element_and_subtract(list)

