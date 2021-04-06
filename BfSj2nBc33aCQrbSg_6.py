
def truncatable(n):
  def isprime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    f = 5
    m = int(n**0.5)
    while f <= m:
      if n%f == 0: return False
      if n%(f+2) == 0: return False
      f += 6
    return True
  
  if '0' in list(str(n)): return False
  left_n,right_n = str(n),str(n)
  for side in ['left','right']:
    while len(eval(side+'_n')) > 0:
      if isprime(int(eval(side+'_n'))):
        if side == 'left': left_n = left_n[1:]
        if side == 'right': right_n= right_n[:-1]
      else:
        break
  
  if (len(left_n) == 0) and (len(right_n) == 0):
    return 'both'
  elif len(left_n) == 0:
    return 'left'
  elif len(right_n) == 0:
    return 'right'
  else:
    return False

