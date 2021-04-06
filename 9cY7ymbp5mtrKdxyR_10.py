
import math as m
from itertools import zip_longest as zl
def encryption(txt):
  pt = txt.replace(" ","")
  lt = len(pt)
  rw = m.ceil(m.sqrt(lt))
  gd = (pt[x:x+rw] for x in range(0,lt,rw))
  tp = zl(*(x for x in gd), fillvalue="")
  return " ".join("".join(x) for x in tp)

