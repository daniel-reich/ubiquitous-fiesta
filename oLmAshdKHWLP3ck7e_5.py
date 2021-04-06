
def min_difference_pair(nums):
  n = sorted(nums)
  m = (min(abs(x-y) for x,y in zip(n,n[1:])))
  return (min([[x,y] for x,y in zip(n,n[1:]) if abs(x-y) == m]))

