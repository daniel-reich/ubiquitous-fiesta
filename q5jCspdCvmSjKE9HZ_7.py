
def determine_if_prime(n):
  if n == 1:
    return False
  if n == 2:
    return True
  for f in range(2, int(n**0.5)+1 ):
    if n % f == 0:
      return False
  return True
  
pf = [] 
def prime_factorization(n):
  global pf
  for f in range(2, int(n**0.5)+1 ):
    if determine_if_prime(f) == True and n % f == 0:
      pf.append(f)
      return prime_factorization(n/f)
  pf.append(n)
  
  PF = pf
  pf = []
  return PF
  
def max_occur(lists, n):   # given list of lists, determine max # of times 'n' appears in any sublist
  counts = []
  for sublist in lists:
    counts.append( sublist.count(n) )
  return max(counts)      
​
def lcm_of_list(numbers):
  all_pf = []
  unique_factors = []
  
  for n in numbers:
    all_pf.append( prime_factorization(n) )
    unique_factors += prime_factorization(n)
  unique_factors = list( set(unique_factors) )
  
  exponents = []
  for f in unique_factors:
    exponents.append( max_occur(all_pf, f) )
    
  LCM = 1
  
  for i in range( len(unique_factors) ):
    LCM *= ( unique_factors[i] ** exponents[i] )
  return LCM

