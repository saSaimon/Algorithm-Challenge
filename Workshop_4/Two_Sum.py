def two_sum(nums, target):
    hash_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_map:
            return [hash_map[complement], i]
        else:
            hash_map[num] = i
    return []

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))