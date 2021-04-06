
def common_last_vowel(txt):
  w = txt[::-1]
  for i in w:
    if i.lower() in 'aeiou':
      return str(i.lower())

