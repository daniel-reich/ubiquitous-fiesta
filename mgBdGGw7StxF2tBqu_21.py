
def duplicates(txt):
  a = [char for char in txt if txt.count(char) > 1]
  return len(a) - len(set(a))

