
def absolute(txt):
  words = txt.split()
  for i in range(len(words)):
    if words[i].lower() == 'a':
      words[i] = words[i]+'n absolute'
  return ' '.join(words)

