
s=[[1]]
​
def bell(n):
  global s
  while n>len(s):
    memn=len(s[-1])
    s+=[[s[-1][-1]]]
    for i in range(memn):s[-1]+=[s[-2][i]+s[-1][i]]
  return s[n-1][n-1]

