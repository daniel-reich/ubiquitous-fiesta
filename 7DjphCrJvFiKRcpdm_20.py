
def covered_integers(lst):
  nums = []
  for item in lst:
    for i in range(item[0], item[1] + 1):
      if not(i in nums):
        nums.append(i)
  return(len(nums))

