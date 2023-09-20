
def reverse_string(word:str):
    final_word = ""
    for i in range (len(word)-1,-1,-1):
        final_word += word[i]
    print(final_word)
reverse_string('Sadiq')
