
from string import ascii_lowercase
​
​
def missing_letter(txt):
    lowest_index = ascii_lowercase.index(txt[0])
    highest_index = ascii_lowercase.index(txt[-1])
    for ch in ascii_lowercase[lowest_index:highest_index + 1]:
        if ch not in txt:
            return ch
    return 'No Missing Letter'

