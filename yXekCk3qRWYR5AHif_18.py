
def vow_replace(word, vowel):
  res = ""
  for ch in word:
    if ch in 'aeiou':
      res += vowel
    else:
      res += ch
  return res

