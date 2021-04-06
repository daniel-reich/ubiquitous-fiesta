
def sum_of_vowels(sentence):
  sentence = list(sentence)
  x = 0
  for i in sentence:
    if i.lower() == "a":
      x += 4
    elif i.lower() == "e":
      x += 3
    elif i.lower() == "i":
      x += 1
  return x

