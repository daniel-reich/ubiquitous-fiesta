
def smith_type(number):
  def digital_root(n):
    t = isinstance(n, int)
    if t == True:
      l = list(str(n))
    else:
      l = n
​
    while len(l) > 1:
      s = 0
      for item in l:
        i = int(item)
        s += i
      l = list(str(s))
    
    return int(l[0])
  def is_prime(n):
    if n < 2:
      return False
    prime = True
    for num in range(2, n):
      r = n % num
      if r == 0:
        prime = False
        break
    
    return prime
  def prime_factors(n):
​
    factors = []
​
    
    
    for num in range(2, int(n/2) + 1):
      r = n % num
      while r == 0:
        factors.append(num)
        n = n/num
        r = n % num
      
    if n != 1:
      factors.append(int(n))
    
    return factors
​
  p_test = is_prime(number)
  if p_test == True:
    return "Trivial Smith"
  if number == 1:
    return "Not a Smith"
  drn = digital_root(number)
  pf = prime_factors(number)
  drp = digital_root(pf)
​
  if drn == drp:
    smith_num = True
  else:
    smith_num = False
    return "Not a Smith"
  
  n1 = number - 1
  n2 = number + 1
​
  relationship = None
​
  p = is_prime(n1)
  drn1 = digital_root(n1)
  pfn1 = prime_factors(n1)
  drp1 = digital_root(pfn1)
  if drn1 == drp1:
    relationship = ['Oldest']
  else:
    
    p2 = is_prime(n2)
    drn2 = digital_root(n2)
    pfn2 = prime_factors(n2)
    drp2 = digital_root(pfn2)
​
    if drn2 == drp2:
      relationship = ['Youngest']
  
  if relationship == None:
    relationship = ['Single']
  
  relationship.append('Smith')
​
  tr = ' '.join(relationship)
​
  return tr

