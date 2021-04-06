
def remove_enemies(names, enemies):
  return sorted(list(set(names)-set(enemies)),key=names.index)

