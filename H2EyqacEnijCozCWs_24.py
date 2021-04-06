
def first_n_vowels(txt, n):
  l = []
  for i in txt:
    if i in 'aeiou':
      l.append(i)
  if n > len(l):
    return "invalid"
  else: 
    return "".join(l[:n])

