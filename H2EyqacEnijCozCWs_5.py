
def first_n_vowels(txt, n):
  v = 'aeiou'
  vowels = []
  for i in txt:
    if i in v:
      vowels.append(i)
  if len(vowels) < n:
    return "invalid"
  else:
    return ''.join(vowels[:n])

