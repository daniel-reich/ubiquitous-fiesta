
from collections import defaultdict
def swap_dict(dic):
  result = defaultdict(list)
  for key in dic:
    result[dic[key]].append(key)
  return result

