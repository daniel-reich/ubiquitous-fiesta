
import functools
def title_to_number(s):
  def convert(string):
    list1 = []
    list1[:0] = string
    return list1
  rev = list(reversed(convert(s)))
  i = 0
  while i < len(rev):
    rev[i] = (ord(rev[i]) - 64) * 26 ** i
    i += 1
  return functools.reduce(lambda a, b: a + b, rev)

