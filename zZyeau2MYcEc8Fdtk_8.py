
def round_number(num, n):
  first = 0
  second = 0
  for i in reversed(range(num+1)):
    if i % n == 0:
      first = i
      break
  for i in range(num,num+n+1):
    if i % n == 0:
      second = i
      break
  return first if num - first < abs(num - second) else second

