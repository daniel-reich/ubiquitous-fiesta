
def remove_enemies(names, enemies):
  for enemy in enemies:
    while enemy in names:
      names.remove(enemy)
  return names

