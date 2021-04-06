
def pyramidal_string(string, t):
  n = len(string); i = 1
  while n > 0:
    n -= i; i += 1
  if n:
    return 'Error!'
​
  res = []
  if t == 'REG':
    i = 0; j = 1; k = 1
    while i+j <= len(string):
      res.append(' '.join(string[i:i+j]))
      i += j; j += 1
  else:
    i, j = 0, i-1
    while j >= 1:
      res.append(' '.join(string[i:i+j]))
      i += j; j -= 1
  return res

