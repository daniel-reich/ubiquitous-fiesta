
def count_eatable_chocolates(t, c):
  t = int(''.join([i for i in t if i.isdigit() or i=='-']))
  c = int(''.join([i for i in c if i.isdigit() or i=='-']))
  if t<=0 or c<=0:
    return 'Invalid Input'
  w = 0
  tot = 0
  while w>=3 or t>=c:
    if w>=3:
      w-=2
      tot+=1
    elif t>=c:
      t-=c
      w+=1
      tot+=1
  return tot

