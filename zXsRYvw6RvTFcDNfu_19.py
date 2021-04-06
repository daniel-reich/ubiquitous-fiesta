
def ruth_aaron(n):
  def pf(x):
    output = []
    for i in range(2, x+1):
      while not x % i:
        output.append(i)
        x //= i
    return [sum(set(output)), sum(output)]
    
  loo, loop = {0: "Aaron", 1: "Ruth"}, 0
  for x in range(n-1,n+1):
    if pf(x) == pf(x+1):
      return [loo.get(loop), 3]
    elif pf(x)[0] == pf(x+1)[0]:
      return [loo.get(loop), 1]
    elif pf(x)[1] == pf(x+1)[1]:
      return [loo.get(loop), 2]
    else:
      loop += 1
  return False

