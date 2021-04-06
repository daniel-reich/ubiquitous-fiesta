
from itertools import takewhile,dropwhile
def compress(c):
  if not c:
    return ""
  if len(c) == 1:
    return c[0]
  string = ''.join(list(takewhile(lambda x: x == c[0],c)))
  if len(string) == 1:
    return c[0] + compress(c[1::])
  return c[0] + str(len(string)) + compress(list(dropwhile(lambda x: x == c[0],c)))

