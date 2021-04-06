
def num_ways(n, s):
  if n==0: return 1
  nums = [1]
  for i in range(1, n+1):
    total = 0
    for j in s:
      if i-j>=0: total+=nums[i-j]
    nums.append(total)
  return nums[n]

