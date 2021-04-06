
from collections import OrderedDict
​
def remove_dups(lst):
    return list(OrderedDict.fromkeys(lst))

