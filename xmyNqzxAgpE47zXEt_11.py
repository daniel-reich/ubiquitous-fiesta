
def is_alphabetically_sorted(sentence):
  sentence = sentence.translate(str.maketrans(',.','  '))
  return any("".join(sorted(word))==word and len(word)>2 for word in sentence.lower().split())

