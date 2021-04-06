
import re
​
def find_and_remove(dct):
  result = {}
  k = list(dct.keys())
  for i in range(len(k)):
    item = k[i]
    res = {}
    k2 = list(dct[item].keys())
    for j in range(len(k2)):
      item2 = k2[j]
      if not (re.match(r'[a-z]', dct[item][item2])):
        res[item2] = int(dct[item][item2])
    result[item] = res
  return result

