def is_almost_palindrome(s):
    # Function to check if a string is a palindrome
    def is_palindrome(string):
        return string == string[::-1]

    # Check if the string itself is a palindrome
    if is_palindrome(s):
        return True

    # Try removing each character one by one and check if the resulting string is a palindrome
    for i in range(len(s)):
        modified_s = s[:i] + s[i + 1:]
        if is_palindrome(modified_s):
            return True

    return False

# Test cases
print(is_almost_palindrome("rakdar"))   # True
# print(is_almost_palindrome("radario"))  # False

#string slicing practice
# value = 'saimon'
# # print(value[:5])
# # print(value[3:])
# print(value[1:2])
# # for i in range(len(value)):
# #     print(value[:i])
# #     print(value[i:])
# #     # print(value[:i] +':'+ value[i:])
# # print(value[::-1])
