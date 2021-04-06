
def vowels(string):
  vowel = 0
  letters = list(string)
  for i in letters:
    if i == 'a':
      vowel = vowel + 1
    if i == 'e':
      vowel = vowel + 1
    if i == 'i':
      vowel = vowel + 1
    if i == 'o':
      vowel = vowel + 1
    if i == 'u':
      vowel = vowel + 1
  return vowel

