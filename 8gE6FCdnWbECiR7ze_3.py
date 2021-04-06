
def prime_facs(n):
  res,i = [],2
  while i*i < n:
    while not n%i:
      res.append(i) 
      n //= i
    i += 1
  if n > 1: 
    res.append(n)
  return res
​
def digiSum(i):
  if i < 10:
    return i
  return digiSum(sum(map(int,list(str(i)))))
​
def smith_type(number):
  prfac,ans = prime_facs(number), 'Single Smith'
  if len(prfac) == 1:
    ans = 'Trivial Smith'
  elif digiSum(sum(prfac)) != digiSum(number):
    ans = "Not a Smith"
  else:
    lprfac,hprfac = prime_facs(number-1),prime_facs(number+1)
    if len(lprfac) > 1 and digiSum(sum(lprfac)) == digiSum(number-1):
      ans = 'Oldest Smith'
    elif len(hprfac) > 1 and digiSum(sum(hprfac)) == digiSum(number+1):
      ans = 'Youngest Smith'
  return ans

