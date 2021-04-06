
def partially_hide(phrase):
  if len(phrase) <2:
    return phrase
  words = []
  for word in phrase.split():
    word = word[0] + '-'*(len(word)-2) + word[-1]
    words.append(word)
  return ' '.join(words)

