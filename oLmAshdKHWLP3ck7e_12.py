
def min_difference_pair(nums):
  lst = sorted(nums)
  lst = [[a, b] for a, b in zip(lst, lst[1:])]
  lst = min(lst, key=lambda x: x[1] - x[0])
  return lst

