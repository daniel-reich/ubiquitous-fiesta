
import re
def best_friend(txt, a, b):
  A=[x for x in txt.split() if x.count(a)==1]
  return a!=b and sum(bool(re.search(a+b, x)) for x in A)>1

