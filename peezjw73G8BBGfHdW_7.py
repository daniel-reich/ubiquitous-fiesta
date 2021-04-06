
import re
def arithmetic_operation(n):
  n = re.sub(r'\s','',n)
  op = re.findall(r'\D+',n)[0]
  nums = re.findall(r'\d+',n)
  if op == "+":
    return int(nums[0]) + int(nums[1])
  elif op == "*":
    return int(nums[0]) * int(nums[1])
  elif op == "-":
    return int(nums[0]) - int(nums[1])
  else:
    try:
      return int(nums[0]) // int(nums[1])
    except ZeroDivisionError:
      return -1

