
def postfix(expr):
  nums = []
  for n in expr.split():
    if n == '+':
      nums.append(nums.pop() + nums.pop())
    elif n == '-':
      nums.append(nums.pop(-2) - nums.pop())
    elif n == '*':
      nums.append(nums.pop() * nums.pop())
    elif n == '/':
      nums.append(nums.pop(-2) / nums.pop())
    else:
      nums.append(int(n))
  return nums[0]

