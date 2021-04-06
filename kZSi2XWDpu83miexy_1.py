
def post_fix(expr):
  pieces = expr.split()
  nums = [p for p in pieces if p.isnumeric()]
  ops = [p for p in pieces if not p.isnumeric()]
  
  curr = nums[0]
  
  for num,op in zip(nums[1:],ops):
    curr = str(int(eval(curr+op+num)))
  
  return int(curr)

