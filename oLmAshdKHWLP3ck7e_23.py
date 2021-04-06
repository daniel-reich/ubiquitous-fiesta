
def min_difference_pair(nums):
  a = sorted(nums)
  b = ((a[i]-a[i-1], a[i-1], a[i]) for i in range(1, len(a)))
  c = sorted(b, key=lambda x:x[0])
  return [c[0][1], c[0][2]]

