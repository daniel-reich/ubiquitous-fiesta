
def shadow_sentence(a, b):
  a = a.split()
  b = b.split()
  if len(a) != len(b): return False
  for i in range(len(a)):
    if len(a[i]) != len(b[i]): return False
    for l in a[i]:
      if l in b[i]: return False
  return True

