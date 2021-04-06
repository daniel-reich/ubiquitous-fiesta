
import copy
def clone(lst):
  clone = copy.deepcopy(lst)
  lst.append(clone)
  return lst

