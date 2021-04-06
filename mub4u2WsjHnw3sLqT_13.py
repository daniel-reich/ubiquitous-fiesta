
lambda_depth = lambda n: 'edabit' if n == 0 else lambda: lambda_depth(n-1)

