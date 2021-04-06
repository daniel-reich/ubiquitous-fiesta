
def sum_of_vowels(sentence):
  vowels = {
  'a': 4,
  'e': 3,
  'i': 1
  }
  return sum([vowels[i] for i in sentence.lower() if i in vowels])

