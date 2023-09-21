def max_continuous_sum(arr):
    if not arr:
        return 0

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

arr = [-4, 2, -1, 3, 4, 10, 10, -10, -1]
result = max_continuous_sum(arr)
print("Largest continuous sum:", result)
