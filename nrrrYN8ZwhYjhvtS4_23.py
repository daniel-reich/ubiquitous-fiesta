
def extend_vowels(word, num):
  vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
  if type(num) is not int or num < 0:
    return "invalid"
  for vowel in vowels:
    word = word.replace(vowel, vowel*(num + 1))
  return word

