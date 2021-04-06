
def remove_vowels(txt):
  vowels = 'aeiouAEIOU'
  res = ''
  for c in txt:
    if c not in vowels:
      res += c
  
  return res

