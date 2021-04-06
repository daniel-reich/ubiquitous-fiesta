
from random import shuffle
def numbers():
    lst = list(range(1, 6))
    shuffle(lst)
    return int("".join(map(str, lst)))

