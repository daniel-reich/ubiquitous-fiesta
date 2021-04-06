
def truncate(txt, length):
  return ' '.join(x for x in txt.split() if x in txt[:length])

