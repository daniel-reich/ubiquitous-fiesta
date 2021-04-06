
def cap_last(txt):
  return " ".join([word[:-1] + word[-1].upper() for word in txt.split(" ")])

