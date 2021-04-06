
def remove_enemies(names, enemies):
  new_list = []
  for i in names:
    if i  in enemies:
      pass
    else:
      new_list.append(i)
  return new_list

