
def sum_prime(lst):
  primes = sorted(set(sum((prime_facts(n) for n in lst),[])))
  return ''.join('({} {})'.format(str(p), str(sum(n for n in lst if n%p==0))) for p in primes)  
​
def prime_facts(n):
  ans = []
  p=2
  while n>1:
    while n%p==0:
      ans.append(p)
      n//=p
    p+=1
  return ans

