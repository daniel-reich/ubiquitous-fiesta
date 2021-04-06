
def sum_of_vowels(sentence):
  return sum([4 if i == "a" else 3 if i == "e" else 1 if i == "i" else 0 for i in sentence.lower()])

