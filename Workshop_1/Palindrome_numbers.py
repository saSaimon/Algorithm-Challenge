
def palindrome_number(num):

    str_num = str(num)
    reversed_string = str_num[::-1]
    if reversed_string == str_num:
        print('True')
    else:
        print('False')

palindrome_number(541)







