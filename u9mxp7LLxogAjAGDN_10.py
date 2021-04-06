
def factor_sort(nums):
  return [x[0] for x in sorted([[nums[i], len(factors(nums[i]))] for i in range(len(nums))], key = lambda x: (x[1], x[0]), reverse = True)]
  
def factors(n):
  return [x for x in range(1, n+1) if n % x == 0]

