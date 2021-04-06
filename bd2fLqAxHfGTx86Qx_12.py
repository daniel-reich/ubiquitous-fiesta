
def can_complete(initial, word):
  l1 = list(initial)
  l2 = l1.copy()
  for i in range(len(word)):
    if word[i] in l1:
      l1.remove(word[i])
      del l2[0]
      if l1 != l2:
        return False
  if l1 == []:
    return True
  else:
    return False

