
from string import ascii_lowercase as ascl, ascii_uppercase as ascu
​
def caesar_cipher(word, num):
    letter_list = []
    for i in word:
        if i in ascu:
            index = ascu.index(i)
            shifted = index+num-max([i for i in range(0, index+num, len(ascu))])
            letter = ascu[shifted] 
            letter_list.append(letter)          
        elif i in ascl:
            index = ascl.index(i)
            shifted = index+num-max([i for i in range(0, index+num+1, len(ascl))])
            letter = ascl[shifted] 
            letter_list.append(letter)
        else:
            letter_list.append(i)
​
    return "".join(letter_list)

