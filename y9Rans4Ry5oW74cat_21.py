
def min_max(nums):
  nums.sort()
  answers = []
  minimum = nums[0]
  maximum = nums[len(nums) - 1]
  answers.append(minimum)
  answers.append(maximum)
  return answers

