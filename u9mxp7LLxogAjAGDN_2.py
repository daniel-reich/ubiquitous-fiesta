
def factor_sort(nums):
  def factor(n):
    return len([i for i in range(1, n+1) if n%i==0])
  return sorted(sorted(nums, reverse=True), key=factor, reverse=True)

