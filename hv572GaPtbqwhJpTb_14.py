
from math import ceil
​
def elasticize(word):
    rise = list(range(1, ceil(len(word)/2 + 1)))
    fall = rise[::-1][1:]if len(word)%2 else rise[::-1]
    res = ''.join(letter*repeat for letter, repeat in zip(word, rise + fall))
    return res

