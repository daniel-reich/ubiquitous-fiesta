
from itertools import permutations as perms
import random
def numbers():
    lon =  [''.join(n) for n in perms('12345')]
    return int(random.choice(lon))

