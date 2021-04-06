
def sum_of_vowels(sentence):
  v = {'a':4, 'e':3, 'i':1}
  return sum(v[ch] for ch in sentence.lower() if ch in v)

