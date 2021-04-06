
def shadow_sentence(a, b):
  if len(a) != len(b):
    return False
    
  for i, j in zip(a.split(), b.split()):
    if len(i) != len(j) or bool(set(i) & set(j)):
      return False
  return True

