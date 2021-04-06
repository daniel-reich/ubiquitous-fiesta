
def greater_permutation(expr, nums):
  print(expr)
  # build all combinations:
  comb=[ [a,b,c] for a in range(3) for b in range(3) for c in range(3) if  a!=b and a!=c and b!=c  ]
  # build all formulars to test
  out=[expr.replace('a',str(nums[x[0]])).replace('b',str(nums[x[1]])).replace('c',str(nums[x[2]])) for x in comb]
  out.sort(key=eval) # sort formulars by highest value
​
  result=eval(out[-1])
  if result%1==0:
    return out[-1] + ' = ' + str(int(result))
  else:
    return out[-1] + ' = ' + str(round(result,2))

