
def is_valid(txt):
  import collections
  x= (collections.Counter(txt))
  a=[]
  for i in x:
    a.append(x[i])
  a.sort()
  if (max(a)-min(a)<2 and (a[1]==a[len(a)-1] or a[len(a)-2]==a[0]) ):
    return "YES"
  return "NO"

