
def correct_sentences(s):
  words = list(filter(None, s.split()))
  words[0] = words[0].capitalize()
  for i in range(len(words)):
    if words[i][0].isupper():
      words[i-1] += '.'
  return ' '.join(words)

