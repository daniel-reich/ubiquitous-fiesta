
def is_disarium(n):
  num = str(n)
  total = 0
​
  for i in num:
      total += int(i) ** (num.index(i) + 1)
  if(total == n): return True
  else: return False

