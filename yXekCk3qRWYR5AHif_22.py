
def vow_replace(word, vowel):
  a = ''
  for w in word:
    if w in 'aeiou':
      a += vowel
    else:
      a += w
  return a

