
def emphasise(txt):
  return " ".join([word[0].upper() + word[1:].lower() for word in txt.split()])

