
def post_fix(expr):
  nums = [i for i in expr.split() if i.isdigit()]
  ops = [i for i in expr if i in '+-*/'] + [' ']
  result = ''
  for i in range(len(nums)):
    result += nums[i] + ops[i]
  return int(eval(result))

