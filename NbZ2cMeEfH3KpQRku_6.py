
def portion_happy(n):
  if len(n) < 2:
    return 0.0
  count =  1 if n[0] == n[1] else 0 
  count += 1 if n[-1] == n[-2] else 0 
  for i in range(1, len(n) - 1):
    count += 1 if n[i-1] != n[i+1] or n[i] == n[i-1] else 0
  return count/len(n)

