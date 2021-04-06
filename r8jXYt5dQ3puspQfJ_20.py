
def split(txt):
  return ''.join([letter for letter in txt if is_vowel(letter)] + [letter for letter in txt if not is_vowel(letter)])
  
def is_vowel(letter):
  return letter in ['a','e','i','o','u']

