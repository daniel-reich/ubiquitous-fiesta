
def fibo_word(n, f=['b', 'a'], i=0):
  if n < 2: return 'invalid'
  if n == i+2: return ', '.join(f)
  return fibo_word(n, f+[f[i+1]+f[i]], i+1)

