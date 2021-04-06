
def sum_odd_and_even(lst):
  a=[]
  b,c=0,0
  for i in lst:
    if (i%2)==0:
      b=b+i
    else:
      c=c+i
  a.append(b)
  a.append(c)
  return a

