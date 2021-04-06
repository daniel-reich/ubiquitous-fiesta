
def arithmetic_progression(start, diff, n):
 st=''
 for i in range(0,n):
  st=st+str(start)+', '
  start=start+diff
 return st[:-2]

