def count_elements_larger_than_neighbors(arr):
    count = 0

    if len(arr) < 3:
        return count

    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            count += 1

    return count


arr = [2, 56, 7, 21, 22, 19, 26]
result = count_elements_larger_than_neighbors(arr)
print("Number of elements larger than neighbors:", result)
