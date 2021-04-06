
import collections 
def can_alternate(s):
  lst = collections.Counter(s)
  if lst["1"] == lst["0"] or lst["0"] + 1 == lst ["1"] or lst["1"] + 1 == lst ["0"]:
    return True
  else:
    return False

