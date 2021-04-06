
def lambda_depth(num):
  return (lambda: lambda_depth(num - 1)) if num else "edabit"

