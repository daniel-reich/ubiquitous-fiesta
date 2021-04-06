
def sum_of_vowels(sentence):
  total = 0
  point = {'a' : 4, 'e' : 3, 'i' : 1, 'o' : 0, 'u' : 0}
  vowels = ['a', 'e', 'i', 'o', 'u']
  sentence = sentence.lower()
  for x in sentence:
    if x in vowels:
      total += point[x]
  return total

