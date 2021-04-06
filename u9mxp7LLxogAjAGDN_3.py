
def factor_sort(nums):
  fac = []
  
  for n in nums:
    count = 0
    for i in range(1,n+1):
      if n%i==0: count = count + 1
    fac.append(count)
  return [x for (y,x) in sorted(zip(fac,nums),reverse=True)]

