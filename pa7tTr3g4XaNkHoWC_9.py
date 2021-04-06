
def pig_latin_sentence(sentence):
  res = []
  for word in sentence.split():
    first = min([i for i, x in enumerate(word) if x in 'aeiou'])
    if first == 0:
      word = word + 'way'
    else:
      word = word[first:] + word[:first] + 'ay'
    res.append(word)
  return ' '.join(res)

