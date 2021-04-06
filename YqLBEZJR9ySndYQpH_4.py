
def staircase(n):
  stairs = ""
  steps = 1
  if n < 0:
    stairs += "#" * -n + "\n"
    for step in range(1,-n-1):
      stairs += "_" * step + "#" * (-n - step) + "\n"
    stairs += "_" * (-n - 1) + "#"
  else:
    for step in range(1,n):
      stairs += ("_" * (n-step)) + ("#" * step) + "\n"
    stairs += "#" * n
  return stairs

