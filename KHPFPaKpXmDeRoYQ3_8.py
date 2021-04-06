
def check_score(s):
  d={'#':5,'O':3,'X':1,'!':-1,'!!':-3,'!!!':-5}
  s = [i for j in s for i in j]
  ret = sum([d[i] for i in s])
  return ret if ret>0 else 0

