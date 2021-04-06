
def consecutive_sum(n):
  lst = list(range(1,n//2+2))
  for i in range(len(lst)):
    szum = 0
    for j in range(i,len(lst)):
      szum += lst[j]
      if szum == n:
        return True
      if szum > n:
        break
  return False

