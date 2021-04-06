
def abbreviate(sentence, n= 4):
  abb = []
  for word in sentence.split():
    if len(word) >= n:
      abb.append(word[0])
  return ''.join(abb).upper()

