
from itertools import zip_longest
def vertical_txt(txt):
  return list(map(list, zip_longest(*txt.split(), fillvalue=' ')))

