def remove_vowels(word:str):
    vowels= 'a', 'e', 'i', 'o', 'u', 'y'
    new_wrod= ""
    for i in word:
        if i in vowels:
            new_wrod = new_wrod+ ''
        elif i == ' ':
            new_wrod =new_wrod+''
        else:
            new_wrod = new_wrod+i
    print(new_wrod)
remove_vowels('hello wordl, how are you doing?')




