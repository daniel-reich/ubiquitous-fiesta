
from itertools import zip_longest
def meme_sum(a, b):
  return int("".join(str(int(x) + int(y))[::-1] for x,y in \
    zip_longest(str(a)[::-1], str(b)[::-1], fillvalue=0))[::-1])

