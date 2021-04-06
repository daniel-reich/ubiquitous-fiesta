
def express_factors(n):
​
  def is_prime(num):
    if num < 2:
      return False
    else:
      for n in range(2, num):
        if num % n == 0:
          return False
      return True
  def exponents(prime, goal):
    e = {}
    n = 1
​
    while prime ** n <= goal:
      e[n] = prime ** n
​
      n += 1
    
    return e
  def check_for_exponent(dicts, goal):
    for num in dicts.keys():
      dic = dicts[num]
      for val in dic.values():
        if val == goal:
          for k in dic.keys():
            if dic[k] == val:
              return [num, k]
    return False
  def format_exponent(exponent):
    base = exponent[0]
    expo = exponent[1]
​
    if expo == 1:
      return str(base)
    else:
      return '{}^{}'.format(base, expo)
  def find_exponent_in_divs(divisors):
    divs = list(set(divisors))
    exponents = []
    for div in divs:
      if divisors.count(div) > 1:
        exponents.append([div, divisors.count(div)])
        for n in range(divisors.count(div)):
          divisors.pop(divisors.index(div))
    if len(exponents) == 0:
      return False
    else:
      new_exponents = [format_exponent(exponent) for exponent in exponents]
      return new_exponents, divisors
​
​
  primes = {}
​
  for num in range(n+1):
    if is_prime(num) == True:
      primes[num] = exponents(num, n)
  
  cfe = check_for_exponent(primes, n)
  divisors = []
  c = 0
  
  while cfe == False and c < 1000:
    for num in reversed(sorted(list(primes.keys()))):
      if n % num == 0:
        divisors.append(num)
        n = n // num
        break
    cfe = check_for_exponent(primes, n)
    c += 1
 # print(divisors)
  poss_exponent = find_exponent_in_divs(divisors)
​
  #print(poss_exponent, divisors)
​
  if poss_exponent != False:
    tr = [format_exponent(cfe)] + [n for n in poss_exponent[0]] + [str(i) for i in sorted(poss_exponent[1])]
  else:
    tr = [format_exponent(cfe)] + [str(i) for i in sorted(divisors)]
  
  try:
    return ' x '.join(tr)
  except TypeError:
    return ' x '

