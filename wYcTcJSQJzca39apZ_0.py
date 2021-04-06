
def truncate(txt, length):
  return " ".join([word for word in txt[:length].split() if word in txt.split()])

