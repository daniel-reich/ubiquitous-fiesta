
import re
def count_same_ends(txt):
  return sum((w[0]==w[-1] and len(w)>1) for w in re.findall(r'\w+',txt.lower()))

