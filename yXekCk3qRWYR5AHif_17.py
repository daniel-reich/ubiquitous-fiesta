
def vow_replace(word, vowel):
  letters = []
  for char in word:
    if char.lower() in 'aeiou':
      letters.append(vowel)
    else:
      letters.append(char)
  return ''.join(letters)

