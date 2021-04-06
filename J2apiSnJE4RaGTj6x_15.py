
from collections import OrderedDict
find_broken_keys=lambda a,b:list(OrderedDict.fromkeys(x for i,x in enumerate(a)if x!=b[i]))

