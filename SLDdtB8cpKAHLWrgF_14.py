
def greater_permutation(expr, nums):
  a,b,c = nums
  expr = expr.translate({ord(l):"{}" for l in "abc"})
  
  perm = [[a,b,c],[a,c,b],[b,a,c],[b,c,a],[c,a,b],[c,b,a]]
  poss = [expr.format(*per) for per in perm]
  largest = sorted(poss, key = eval)[-1]
  
  v = eval(largest)
  value = int(v) if v%1==0 else round(v,2) 
  
  return largest + " = " + str(value)

