
def fibo_word(n):
  if n < 2: return 'invalid'
  res = ['b', 'a']
  for a in range(3, n + 1):
    res.insert(a, res[a - 2] + res[a - 3])
  return ', '.join(res)

