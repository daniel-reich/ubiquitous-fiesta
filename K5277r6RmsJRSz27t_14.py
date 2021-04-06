
def emphasise(txt):
  lst = txt.split()
  return " ".join(word[0].upper()+word[1:].lower() for word in lst)

