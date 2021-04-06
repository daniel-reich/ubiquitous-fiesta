
def shadow_sentence(a, b):
  if len(a)!=len(b) or a==b:return False
  a=a.split()
  b=b.split()
  for i in range(len(a)):
    if not all([j not in b[i] for j in a[i]]):return False
  return True

