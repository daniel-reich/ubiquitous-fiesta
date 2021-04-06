
def logarithm(base, num):
  if base<2 or num<2: return 'Invalid'
  ans = 1
  prod = base
  while prod!=num:
    prod*= base
    ans+=1
  return ans

