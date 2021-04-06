
def factor_sort(nums):
  return sorted(nums, key=lambda n:100*sum(n%x==0 for x in range(1,n+1))+n)[::-1]

