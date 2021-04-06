
def twins(nums):
  for index, _  in enumerate(nums):
    if sum(nums[:index]) == sum(nums[index:]):
      return index

