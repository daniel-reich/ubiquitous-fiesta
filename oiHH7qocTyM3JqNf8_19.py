
from string import ascii_letters
​
def move(ex):
    lst_ex = []
​
    for letter in ex:
        if letter in ascii_letters:
            lst_ex.append(ascii_letters[(ascii_letters.index(letter) + 1)])
​
    new_ex = "".join(lst_ex)
​
    return new_ex

