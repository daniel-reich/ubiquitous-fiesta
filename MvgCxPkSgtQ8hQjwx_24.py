
def remove_vowels(txt):
  for i in txt:
    if i in 'aeiouAEIOU':
      txt = txt.replace(i, '')
  return txt

