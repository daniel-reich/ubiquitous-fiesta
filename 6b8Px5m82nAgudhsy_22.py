
from itertools import permutations
​
​
def next_number(num):
    try:
        perms = list(permutations(str(num)))
        j = ["".join(i) for i in perms]
        inted = [int(i) for i in j]
        return sorted([i for i in inted if i > num])[0]
    except IndexError:
        return num

