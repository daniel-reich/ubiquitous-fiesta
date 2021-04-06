
from string import ascii_lowercase as lower
from string import ascii_uppercase as upper
​
def caesar_cipher(s, k):
    trans = str.maketrans(lower, lower[k%26:]+lower[:k%26])
    trans.update(str.maketrans(upper, upper[k%26:]+upper[:k%26]))
    return s.translate(trans)

