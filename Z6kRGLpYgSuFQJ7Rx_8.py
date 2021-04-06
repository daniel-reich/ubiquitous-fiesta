
def find_longest(sentence):
  for char in sentence:
    if not char.isalpha() and char != ' ':
      sentence = sentence.replace(char, ' ')
  result = sorted(sentence.split(), key=len, reverse=True)
  return result[0].lower()

