
def remove_enemies(names, enemies):
  for enemy in enemies:
    for name in names:
      if name == enemy:
        names.remove(name)
        
  return names

