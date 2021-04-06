
def sentence(words):
  for i in range(len(words)):
    if words[i][0] in 'aeiou':
      words[i] = 'an '+words[i]
    else:
      words[i] = 'a '+words[i]
  return ', '.join(words[:-1]).capitalize()+' and '+words[-1]+'.'

