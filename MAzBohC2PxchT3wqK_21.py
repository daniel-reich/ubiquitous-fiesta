
def shadow_sentence(a, b):
  if len(a.split()) != len(b.split()):
    return False
  for x, y in zip(a.split(), b.split()):
    if len(x) != len(y):
      return False
    for char in x:
      if char in y:
        return False
  return True

