
def shared_letters(a, b):
  lst =[]
  for i in a.lower():
    if i in b.lower():
      lst.append(i)
  return ''.join(sorted(set(lst)))

