
def fibo_word(n):
  if n < 2:
    return 'invalid'
    
  l = ['b', 'a']
  for i in range(n-2):
    l.append(l[-1] + l[-2])
  return ', '.join(l)

