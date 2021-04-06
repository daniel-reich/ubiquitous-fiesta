
def is_valid(txt):
  a = sorted(txt.count(i) for i in set(txt))
  if len(set(a)) == 1:
      return "YES"
  else:
      b = a[-1]-a[0]==1 and a.count(a[-1])==1
      return "YES" if b else "NO"

