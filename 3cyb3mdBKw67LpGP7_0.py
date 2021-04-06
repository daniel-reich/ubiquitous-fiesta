
from itertools import groupby
​
def numbers_need_friends_too(n):
  result = ''
  for key, group in groupby(str(n)):
    length = len(list(group))
    result += 3 * key if length is 1 else length * key
  return int(result)

