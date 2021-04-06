
def perrin(n):
  if n==0: return 3
  elif  n==1: return 0
  elif  n==2: return 2
  else: return perrin(n-2)+perrin(n-3)

