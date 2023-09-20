def is_anagram(word_1, word_2):
    a = True
    for i in word_1:
        if i in word_2:
            a = True
        else:
            a = False
    print(a)


is_anagram('abcdef', 'feabcd')