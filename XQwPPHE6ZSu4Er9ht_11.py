
def is_economical(n):
  def fac(x):
    ans = []
    i = 2
    while x != 1:
      if x % i == 0:
        ans.append(i)
        x /= i
      else: i += 1
    count = 0
    for j in set(ans): count += ((len(str(j)) + len(str(ans.count(j)))) 
                       if ans.count(j) > 1 else len(str(j)))
    return count
  if len(str(n)) == fac(n): return 'Equidigital'
  if len(str(n)) < fac(n): return 'Wasteful'
  return 'Frugal'

