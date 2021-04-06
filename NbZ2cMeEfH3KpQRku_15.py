
def percentage_happy(nums):
  unhappy = nums[:2] == [0,1] or nums[:2] == [1,0]
  unhappy += nums[-2:] == [0,1] or nums[-2:] == [1,0]
  for i in range(len(nums)-2):
    unhappy += nums[i:i+3] == [0,1,0] or nums[i:i+3] == [1,0,1]
  return 1 - unhappy / len(nums)

