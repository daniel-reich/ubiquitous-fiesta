
def remove_enemies(names, enemies):
  friendly = []
  for name in names:
    if name not in enemies:
      friendly.append(name)
  return friendly

