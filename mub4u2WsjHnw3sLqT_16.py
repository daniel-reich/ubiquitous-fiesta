
def lambda_depth(n):
  return 'edabit' if not n else lambda: lambda_depth(n-1)

