
def min_difference_pair(nums):
  lst = sorted(nums)
  lstd = [lst[i+1]-lst[i] for i in range(len(lst)-1)]
  for i in range(len(lst)-1):
    if lst[i+1] - lst[i] == min(lstd):
      return [lst[i],lst[i+1]]

