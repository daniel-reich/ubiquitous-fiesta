
 def first_n_vowels(txt, n):
  v = [i for i in txt if i in 'aeiou']
  return 'invalid' if n>len(v) else ''.join(v[:n])

