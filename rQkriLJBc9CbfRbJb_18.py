
def indexOfCaps(word):
  result = []
  for letter in word:
    if letter.isupper():
      result.append(word.index(letter))
  return result

