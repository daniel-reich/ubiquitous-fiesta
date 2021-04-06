
import itertools as it
def extract_primes(num):
  s = str(num)
  combos = it.combinations(list(range(len(s)+1)), 2)
  nums = [int(s[a:b]) for a,b in combos if s[a]!='0']
  return sorted(i for i in nums if prime(i))
​
def prime(n):
  if n < 3: return n==2
  return not [i for i in range(2,int(n**0.5)+1) if not n%i]

