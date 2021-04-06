
import string
​
def add_letters(a):
    total = sum((string.ascii_lowercase.index(letter)+1 for letter in a))
    return string.ascii_lowercase[total-1] if total < 26 else string.ascii_lowercase[(total-1)%26]

