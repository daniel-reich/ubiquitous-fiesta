
import itertools
​
​
def next_number(num):
    r = [x for x in str(num)]
    lol = list(set(sorted([int("".join(i)) for i in list(itertools.permutations(r))])))
    lol.sort()
    if lol.index(num) == len(lol)-1:
        return num
    else:
        return lol[lol.index(num)+1]

