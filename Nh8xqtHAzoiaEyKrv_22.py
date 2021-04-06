
def correct_sentences(s):
  words = s.split()
  for i in range(len(words)):
    if words[i] == words[0]:
      words[i] = words[i].title()
    if words[i][0].isupper():
      words[i - 1] = words[i - 1] + '.'
  return ' '.join(words)

