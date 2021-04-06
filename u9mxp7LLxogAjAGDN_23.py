
def factor_sort(nums):
  return sorted(nums, key=num_factors,reverse=True)
  
def num_factors(num):
  s = sum(num % fac == 0 for fac in range(1,num))
  return (s,num)

