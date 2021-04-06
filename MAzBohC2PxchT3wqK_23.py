
def shadow_sentence(a, b):
  found_shadow = True
  if len(a) != len(b):
    return False
  else:
    a, b = a.split(), b.split()
    for i in range(len(a)):
      if len(a[i]) != len(b[i]):
        found_shadow = False
      elif len(a[i]) == len(b[i]):
        for j in range(len(a[i])):
          if a[i][j] in b[i]:
            found_shadow = False
  return found_shadow

