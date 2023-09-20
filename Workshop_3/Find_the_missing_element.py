import random
def find_the_missing_num(list):

    list_2 = random.sample(list, len(list))

    random_element = random.choice(list_2)
    print(random_element)
    print(list_2)
    list_2.remove(random_element)
    print(list_2)

    for n in list:
        if n not in list_2:
            print(f'the missing integer is {n}.')



list = [0,1,2,3,4,5,6,7,8,9]
find_the_missing_num(list)