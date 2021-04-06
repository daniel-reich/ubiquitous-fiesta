
def left_slide(row):
  nums = [i for i in row if i]
  newRow = []
  while nums:
    cur = nums.pop(0)
    if nums and cur == nums[0]: 
      cur += nums.pop(0)
    newRow.append(cur)
  return newRow + [0] * (len(row) - len(newRow))

