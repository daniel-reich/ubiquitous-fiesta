
def first_n_vowels(txt, n):
  v,s='aeiou',''
  for i in txt:
    if i in v:
      s+=i
  if n>len(s):
    return 'invalid'
  return s[:n]

