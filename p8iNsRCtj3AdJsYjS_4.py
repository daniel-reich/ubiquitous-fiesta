
from functools import reduce
def title_to_number(s):
  return reduce(lambda acc, ch: acc*26 + (ord(ch) - 64), s, 0)

