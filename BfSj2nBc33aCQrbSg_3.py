
import numpy
from math import floor
def primesfrom3to(n):
    """ Returns a array of primes, 3 <= p < n """
    sieve = numpy.ones(n//2, dtype=numpy.bool)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = False
    return 2*numpy.nonzero(sieve)[0][1::]+1
  
def pruneNum(num):
  if (len(str(num))==1): return ''
  numb = list(str(num))
  numb.remove(numb[0])
  return int(''.join(numb))
  
def checkRL(num, rl, primes):
  if (rl=="r"):
    while len(list(str(num)))!=1:
      num = floor(num/10)
      if (num not in primes and num!=2): return False
    return True
  else:
    while len(list(str(num)))!=1:
      num = pruneNum(num)
      if (num not in primes and num!=2): return False
    return True
  
def truncatable(n):
  answer, primes = [], primesfrom3to(n+1)
  checkedR, checkedL = checkRL(n, "r", primes), checkRL(n, "l", primes)
  if ('0' in list(str(n))): return False
  elif (n not in primes): return False
  if (checkedR==True): answer.append("right")
  if (checkedL==True): answer.append("left")
  if ("right" in answer and "left" in answer): answer = ["both"]
  if (answer == []): answer=[False]
  return answer[0]

