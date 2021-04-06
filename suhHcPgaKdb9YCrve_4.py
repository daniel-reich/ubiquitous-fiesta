
def even_or_odd(s):
  m=list(map(int,s))
  ms=sum(x for x in m if x%2)-sum(x for x in m if not x%2)
  return ['Even and Odd are the same','Odd is greater than Even','Even is greater than Odd'][(ms>0)-(ms<0)]

