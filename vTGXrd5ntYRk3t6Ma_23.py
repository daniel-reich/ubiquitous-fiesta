
def is_isogram(txt):
  return len(list(txt.lower())) == len(set(list(txt.lower())))

