
def remove_enemies(names, enemies):
  while True:
    if not enemies:
      return names
    for name in enemies:
      if not names.count(name):
        flag = True
      else:
        flag = False
        names.remove(name)
    if flag:
      return names

