
def replace_vowel(word):
  for x in 'aeiou':
    word = word.replace(x,str('aeiou'.index(x)+1))
  return word

