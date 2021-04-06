
def remove_enemies(names, enemies):
  n = []
  for i in names:
    if i not in enemies:
      n.append(i)
  return n

