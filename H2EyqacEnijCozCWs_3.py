
def first_n_vowels(txt, n):
  s = ''
  for i in txt:
    if i in 'aioue':
      s+=i
  return s[:n] if len(s) >= n else 'invalid'

