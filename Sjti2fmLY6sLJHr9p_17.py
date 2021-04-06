
from itertools import groupby
def look_and_say(start, n):
  res = [start]
  while len(res) < n:
    temp = ''
    for k, g in groupby(str(res[-1])):
      num = list(g)
      temp += '{}{}'.format(len(num), num[0])
    res.append(int(temp))
  return res

