
def postfix(expression):
  nums = list()
  for c in expression.split():
    try: nums.append(int(c))
    except:
      nums, a, b = nums[:-2], nums[-2], nums[-1]
      if c == '+': nums.append(a+b)
      elif c == '-': nums.append(a-b)
      elif c == '*': nums.append(a*b)
      elif c == '/': nums.append(a/b)
  return int(nums[0])

