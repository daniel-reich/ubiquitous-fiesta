
def make_title(txt):
  return " ".join(word[0].upper() + word[1:] for word in txt.split(" "))

