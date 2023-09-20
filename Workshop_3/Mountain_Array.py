def isMountainArray(arr):
    n = len(arr)

    # Find the peak of the mountain (maximum element)
    peak_index = arr.index(max(arr))
    print(peak_index)

    # Check if the peak is not the first or last element
    if peak_index == 0 or peak_index == n - 1:
        return False

    # Check if elements are increasing before the peak
    for i in range(peak_index):
        if arr[i] >= arr[i + 1]:
            return False

    # Check if elements are decreasing after the peak
    for i in range(peak_index, n - 1):
        if arr[i] <= arr[i + 1]:
            return False

    return True


# Test cases
print(isMountainArray([3, 5, 5, 4]))  # False
print(isMountainArray([3, 4, 5, 6, 2]))  # True

