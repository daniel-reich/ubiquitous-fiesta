
def perrin(n):
  return [3,0,2][n] if n < 3 else perrin(n-2)+perrin(n-3)

