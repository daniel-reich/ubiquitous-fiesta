
def arithmetic_progression(start, diff, n):
  ans = []
  for i in range(n):
    ans.append(str(start))
    start += diff
  
  return ', '.join(ans)

