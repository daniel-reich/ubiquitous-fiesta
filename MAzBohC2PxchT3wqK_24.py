
def shared_letters(a, b):
  for i in a:
    if i in b: return True
  return False
def shadow_sentence(a, b):
  a = a.split()
  b = b.split()
  if len(a)!=len(b): return False
  for i in range(len(a)):
    if len(a[i])!=len(b[i]): return False
    if shared_letters(a[i], b[i]): return False
  return True

