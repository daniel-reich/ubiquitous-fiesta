
def bridge_shuffle(lst1, lst2):
  shuffled = []
  for i, elem in enumerate(lst1):
    shuffled.append(elem)
    if i < len(lst2):
      shuffled.append(lst2[i])
  if len(lst2) > len(lst1):
    shuffled += lst2[len(lst1):]
  return shuffled

