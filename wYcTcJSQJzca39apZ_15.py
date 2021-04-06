
def truncate(txt, length):
  if length > len(txt):
    return txt
  else:
    idx = (txt + ' ')[:length + 1].rfind(' ')
    return "" if idx == -1 else txt[:idx]

