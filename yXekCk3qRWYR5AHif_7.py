
def vow_replace(word, vowel):
  vowels = ['a', 'e', 'i', 'o', 'u']
  word = list(word)
  for i,char in enumerate(word):
    if char in vowels:
      word[i] = vowel
  return ''.join(word)

