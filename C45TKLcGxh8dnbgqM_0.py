
from string import ascii_lowercase as up, ascii_uppercase as low
​
def caesar_cipher(s, k):
    k %= 26
    return s.translate(str.maketrans(up + low, ''.join((up[k:], up[:k], low[k:], low[:k]))))

