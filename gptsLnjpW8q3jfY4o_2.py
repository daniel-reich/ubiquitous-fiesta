
import re
def Formula(n):
  if n<0: return "1/({})".format(Formula(-n))
  if n==0: return '1'
  pre = '+'.join([str(comb(n,k))+'a^'+str(n-k)+'b^'+str(k) for k in range(0,n+1)])
  prepre = re.sub(r'a\^0|b\^0|\^1(?!\d)','',pre)
  return re.sub(r"(?<!\d)(?<!\^)1(?!\d)",'',prepre)
​
def comb(n,k):
  ans = 1
  for i in range(k): 
    ans = ans*(n-i)//(i+1)
  return ans

