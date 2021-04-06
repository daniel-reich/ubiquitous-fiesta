
def remove_letters(l,w):
  for i in w:
    try:
      l.remove(i)
    except:
      continue
  return l

