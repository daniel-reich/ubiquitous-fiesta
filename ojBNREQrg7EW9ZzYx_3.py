
import re
def count_eatable_chocolates(t,c):
  a,b=map(int,re.findall('-?\d+',t+c))
  if b<1:return'Invalid Input'
  k=s=a//b
  while k>2:n=k//3;s+=n;k-=2*n
  return s

