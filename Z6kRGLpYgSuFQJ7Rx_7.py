
def find_longest(sentence):
  sentence = sentence.replace("'", " ")
  sentence = sentence.replace('.', ' ')
  return sorted([word.lower() for word in sentence.split()],  key = lambda word:len(word))[-1]

