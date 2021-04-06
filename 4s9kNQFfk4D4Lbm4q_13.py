
def ABA(s):
  if s == 'A':
    return 'A'
  start = 'B'
  stop = s
  res = 'A'
​
  for i in range(ord(start), ord(stop) + 1):
    res = res + chr(i) + res
  return(res)

