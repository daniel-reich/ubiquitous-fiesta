
def is_alphabetically_sorted(sentence):
  for x in sentence[:-1].split():
    x = x.lower()
    if ''.join(sorted(list(x))) == x and len(x) >= 3:
      return True
      
  return False

