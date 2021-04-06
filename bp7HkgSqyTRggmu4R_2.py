
def reverse_title(txt):
  return ' '.join(w[0].lower() + w[1:].upper() for w in txt.split())

