
def make_title(txt):
  return ' '.join([word[0].upper() + word[1:len(word)] for word in txt.split()])

