
def truncate(txt, length):
  return txt if len(txt)<=length else ' '.join(txt[:length + 1].split(' ')[0:-1])

