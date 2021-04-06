
def lambda_depth(num=None):
  return "edabit" if num==0 else lambda:lambda_depth(num-1)

