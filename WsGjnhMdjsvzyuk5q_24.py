
def dashed(txt):
  word = ''
  for letter in txt:
    if letter.lower() in 'aeiou':
      word += '-' + letter + '-'
    else:
      word += letter
  return word

