
def first_n_vowels(txt, n):
  v = [x for x in txt if x in 'aeiou' ]
  return 'invalid' if len(v) < n else ''.join(v[:n])

