
def check(lst):
  sor = sorted(lst)
  n = lst.index(sor[0])
  return 'YES' if n>0 and all(sor[i]==lst[(i+n)%len(lst)] for i in range(len(lst))) else 'NO'

