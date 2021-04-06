
import re
def isPrime(n) : 
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
    return True
    
def how_bad(n):
  s=''
  while n>0:
    i = n%2
    n=int(n/2)
    s += str(i)
  lst =[]
  t=0
  if len(re.findall('[1]',s)) % 2 ==0:
    lst.append("Evil")
  else: 
    lst.append("Odious")
  for i in enumerate(re.findall('[1]',s)):
    t = t + int(i[1])*(2**int(i[0]))
  if isPrime(t):
    lst.append("Pernicious")
  return lst

