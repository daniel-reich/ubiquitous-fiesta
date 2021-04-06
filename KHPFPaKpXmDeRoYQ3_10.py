
from collections import Counter
def check_score(s):
  dic = {'#':5,'O':3,'X':1,'!':-1,'!!':-3,'!!!':-5}
  res = sum(sum(dic[k]*v for k,v in Counter(t).items()) for t in s)
  return res if res > 0 else 0

