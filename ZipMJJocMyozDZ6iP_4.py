
def group(l,s):
  k=-(-len(l)//s)
  return[l[i::k]for i in range(k)]

