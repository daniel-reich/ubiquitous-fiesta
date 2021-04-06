
def vow_replace(word, vowel):
  vowels = 'a', 'e', 'i', 'o', 'u'
  new = ''
  for char in word:
    if char in vowels:
      new = new + vowel
    else:
      new = new + char
  return new

