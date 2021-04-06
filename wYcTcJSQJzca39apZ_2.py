
def truncate(txt, length):
  return ' '.join((txt+" X")[:length+2].split()[:-1])

