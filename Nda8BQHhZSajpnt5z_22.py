
def GCD(lst):
  def denominators(nums):
    tr = []
    for num in nums:
      factors = []
      for n in range(1, num + 1):
        if num%n==0:
          factors.append(n)
      tr.append(factors)
    return tr
  def common(lsts):
    c = set()
    
    for lst in lsts:
      for i in lst:
        valid = True
        for l in lsts:
          if i not in l:
            valid = False
            break
        if valid == True:
          c.add(i)
    
    return c
  
  dens = denominators(lst)
  comm = common(dens)
  
  return max(comm)

