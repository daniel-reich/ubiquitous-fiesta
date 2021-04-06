
import collections
def remove_dups(lst):
  return list(collections.OrderedDict.fromkeys(lst))

