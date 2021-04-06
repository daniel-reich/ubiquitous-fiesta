
def first_n_vowels(txt, n):
  r = ''
  for ch in txt:
    if n == 0:
      break;
    if ch in 'aeiou':
      r += ch
      n -= 1
  if n != 0:
    return "invalid"
  return r

