
def emphasise(txt):
  return ' '.join([word[0].capitalize() + word[1:].lower() for word in txt.split(' ') if txt])

