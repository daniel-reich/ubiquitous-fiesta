
def shadow_sentence(a, b):
  a, b = a.split(), b.split()
  if len(a) != len(b):
    return False
  pairs = zip(a, b)
  for pair in pairs:
    if len(pair[0]) != len(pair[1]):
      return False
    for letter in pair[0]:
      if letter in pair[1]:
        return False
  return True

