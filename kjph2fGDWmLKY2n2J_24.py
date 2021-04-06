
def valid_color (color):
  if color[:4] == 'rgb(':
    alpha = False
  elif color[:5] == 'rgba(':
    alpha = True
  else:
    return False
  if alpha:
    nums = color[5:-1].split(',')
  else:
    nums = color[4:-1].split(',')
  nums = [s.strip() for s in nums]
  if alpha and len(nums) != 4:
    return False
  if not alpha and len(nums) != 3:
    return False
  for s in nums:
    if s == '':
      return False
  maxval = 255
  if nums[0][-1] == '%':
    nums = [s[:-1] for s in nums]
    maxval = 100
  nums = [float(n) for n in nums]
  for i in range(3):
    if 0 > nums[i] or nums[i] > maxval:
      return False
  if alpha:
    if nums[3] < 0 or nums[3] > 1:
      return False
  return True

