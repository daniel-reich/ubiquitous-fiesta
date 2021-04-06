
def factor_sort(nums):
  return sorted(nums, key=lambda x: (-sum(x%i == 0 for i in range(1, x+1)), -x))

