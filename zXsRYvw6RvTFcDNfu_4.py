
def ruth_aaron(n):
  def prime(n):
      k = 2
      while k <= n:
          if n%k == 0:
              n //= k
              yield k
          else: k += 1
  def1 = [list(prime(n+i)) for i in range(-1,2)]
  d,e,f = def2 = [sum(set(p)) for p in def1]
  a,b,c = def1 = [sum(p) for p in def1]
​
  i = 0; name = None
  if a == b or d == e: name = 'Aaron'
  if b == c or e == f: name = 'Ruth'
  if len(set(def1)) < 3: i += 2
  if len(set(def2)) < 3: i += 1
  return False if name is None else [name,i]

