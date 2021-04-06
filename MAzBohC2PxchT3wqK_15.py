
def shadow_sentence(a, b):
  if len(a)==len(b):
    for x,y in zip(a.split(), b.split()):
      if len(x)!=len(y) or any(i in y for i in x):
        return False
    return True
  return False

