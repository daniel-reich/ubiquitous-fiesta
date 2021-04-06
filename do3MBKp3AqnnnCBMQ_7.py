
from itertools import permutations
import random
pool = [int(''.join(str(d) for d in perm)) for perm in permutations(range(1,6),5)]
​
def numbers():
  return pool[random.randrange(0,59)]

