
def shared_letters(a, b):
  L = []
  for char in a.lower():
    if char in b.lower() and char not in L:
      L.append(char)
  L.sort()
  return ''.join(L)

