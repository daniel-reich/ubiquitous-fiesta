
import copy
def clone(lst):
    a = copy.copy(lst)
    a.append(lst)
    return a

