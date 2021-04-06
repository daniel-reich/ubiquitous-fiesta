
def sum_of_vowels(sentence):
  codes = {'a': 4, 'e': 3, 'i': 1, 'o': 0, 'u': 0}
  return sum(codes[i] for i in sentence.lower() if i in codes)

