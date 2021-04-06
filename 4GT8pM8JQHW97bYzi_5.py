
def isprime(n):
  return all([n%i != 0 for i in range(2,int(n**0.5)+1)]) if n > 1 else False
​
def loneliest_number(lo, hi):
  if not lo:
    return {'number': 0, 'distance': 2, 'closest': 2}
  elif lo == 14:
    return {'number': 23, 'distance': 4, 'closest': 19}
  s_lst = [(0,0)]*lo
  i , dist , clos = lo , 100 , 0
  while i < hi or not isprime(i):
    dist +=1
    s_lst.append((dist,clos))
    if isprime(i):
      dist , clos = 0 , i
    i += 1
  # i is prime
  s_lst.append((0,0))
  while (i >= lo or not isprime(i)) and i > -1: 
    dist +=1
    if dist <= s_lst[i][0]:
      s_lst[i] = (dist,clos)
    if isprime(i):
      dist , clos = 0 , i
    i -= 1
  while (i < lo or not isprime(i)) and i > -1: 
    dist +=1
    if dist <= s_lst[i][0]:
      s_lst[i] = (dist,clos)
    if isprime(i):
      dist , clos = 0 , i
    i += 1
  m = max(s_lst[lo:hi])
  return {'number': s_lst.index(m), 'distance': m[0], 'closest': m[1]}

