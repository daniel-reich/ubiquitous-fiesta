
from itertools import groupby
​
def clean_up(files, sort):
  return [list(i[1]) for i in groupby(files, lambda x: x.split(".")[int(sort == "suffix")])]

