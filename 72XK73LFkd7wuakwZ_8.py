
def junction_or_self(n):
​
​
  l = [] 
  for i in range(1, n + 1):
    digits = sum(int(j) for j in str(i)) + i
    if digits == n:
      l.append(i)
​
  if not l:
    return 'Self'
  return sorted(l, reverse = True)

