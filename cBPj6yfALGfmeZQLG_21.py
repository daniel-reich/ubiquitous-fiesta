
from itertools import zip_longest
def vertical_txt(txt):
  return [list(a) for a in zip_longest(*txt.split(" "), fillvalue=" ")]

