
def group(l,s):
  k=-(-len(l)//s)
  return[[l[i]for i in range(j,len(l),k)]for j in range(k)]

