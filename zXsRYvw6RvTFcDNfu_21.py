
def ruth_aaron(n):
  def prime_factorize(num):
    def is_prime(num):
      for n in range(2, num):
        if num % n == 0:
          return False
      return True
    factors = []
    if is_prime(num) == True:
      return [num]
    for n in range(2, num):
      if n > num:
        break
      if is_prime(n) == True:
        while num % n == 0:
          factors.append(n)
          num = num/n
    return factors
  class Pair:
​
    def __init__(self, a, b):
      self.a = a
      self.b = b
    
    def one(self):
​
      afactors = list(set(prime_factorize(self.a)))
      bfactors = list(set(prime_factorize(self.b)))
​
      return sum(afactors) == sum(bfactors)
    
    def two(self):
​
      afactors = prime_factorize(self.a)
      bfactors = prime_factorize(self.b)
​
      return sum(afactors) == sum(bfactors)
  
  possible_pairs = {'G': Pair(n-1, n), 'L': Pair(n, n+1)}
  pair_results = {}
​
  for l8r in possible_pairs.keys():
    pair = possible_pairs[l8r]
​
    one = pair.one()
    two = pair.two()
​
    pair_results['{}-1'.format(l8r)] = one
    pair_results['{}-2'.format(l8r)] = two
​
  L = 'Ruth'
  G = 'Aaron'
  
  if True not in pair_results.values():
    return False
  else:
    tr = []
​
    correctnums = []
    correctl8rs = set()
​
    for key in pair_results:
      if pair_results[key] == True:
        key = key.split('-')
        l8r = key[0]
        num = int(key[1])
        correctl8rs.add(l8r)
        correctnums.append(num)
​
    tr.append(eval(list(correctl8rs)[0]))
​
    if len(correctnums) == 2:
      tr.append(3)
    else:
      tr.append(correctnums[0])
    
    return tr

