
def is_alphabetically_sorted(sentence):
  for x in sentence.split():
    x = x.strip('.').strip(',').strip('!')
    if x == ''.join(sorted(x)) and len(x) > 2:
      return True
  return False

