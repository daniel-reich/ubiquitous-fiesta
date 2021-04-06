
def numbers():
    from random import randint
    from itertools import permutations
    buf = set(''.join(x) for x in permutations('12345', 5))
    return int(list(buf)[randint(1, len(buf))])

