
from collections import Counter
def express_factors(n):
  cnt = Counter(prime_facts(n))
  return ' x '.join(str(k)+ ('^'+str(cnt[k]) if cnt[k]>1 else '') for k in sorted(cnt))
​
def prime_facts(n):
  ans = []
  i=2
  while n!=1:
    while n%i==0:
        ans.append(i)
        n//=i
    i+=1
  return ans

