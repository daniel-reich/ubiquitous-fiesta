
import re
def isprime(n):
  return all([n%i != 0 for i in range(2,n)]) if n > 1 else False
​
def extract_primes(num):
  lst = [int(str(num)[i:j]) for i in range(len(str(num))) for j in range(i+1,len(str(num))+1) if str(num)[i] != '0' ]
  return [i for i in sorted(lst) if isprime(i)]

