
def sum_of_vowels(sentence):
  return sum({"a": 4, "e": 3, "i": 1}.get(c, 0) for c in sentence.lower())

