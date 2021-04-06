
def first_n_vowels(txt, n):
  x = ''.join([i for i in txt if i in 'aeiou'][:n])
  if len(x) >= n:
    return x
  return "invalid"

