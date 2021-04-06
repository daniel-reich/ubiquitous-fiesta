
from collections import OrderedDict
def unrepeated(txt):
  return "".join(OrderedDict.fromkeys(txt))

