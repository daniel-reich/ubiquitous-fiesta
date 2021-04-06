
def lambda_depth(num):
  return 'edabit' if not num else lambda : lambda_depth(num - 1)

