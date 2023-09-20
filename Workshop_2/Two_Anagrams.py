
def anagram(word_1, word_2):
    word_1 = word_1.lower()
    word_2 = word_2.lower()

    if  sorted(word_1)==sorted(word_2):
        print(True)
    else:
        print(False)

anagram('cat', 'atc')