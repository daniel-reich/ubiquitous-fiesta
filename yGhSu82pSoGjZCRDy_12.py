
def seesaw(nums):
  if nums == None or len(str(nums)) == 1:
    return 'balanced'
  nums = str(nums)
  if len(str(nums))%2 == 0:
    right_num = nums[int(len(nums)/2):]
    left_num = nums[0:int(len(nums)/2)]
  elif len(str(nums))%2 != 0:
    right_num = nums[-(int(len(nums))-1)//2:]
    left_num = nums[:(int(len(nums))-1)//2]
  if right_num > left_num:
    return 'right'
  elif left_num > right_num:
    return 'left'
  elif right_num == left_num:
    return 'balanced'

