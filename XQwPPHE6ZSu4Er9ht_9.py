
def is_economical(n):
  prime_list = []
  j=n
  for i in range(2,j+1):
    while not j%i:
      prime_list.append(i)
      j /= i
  
  dct = {key:prime_list.count(key) for key in prime_list}
​
  result = sum(len(str(i)) for i in dct.keys()) +\
  sum(len(str(i)) for i in dct.values() if i !=1)
  
  return "Equidigital" if result == len(str(n)) else "Frugal" if result < len(str(n)) else "Wasteful"

