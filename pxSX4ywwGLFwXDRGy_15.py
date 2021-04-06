
def remove_enemies(names, enemies):
  notenemy = []
  for name in names:  
    if name not in enemies:
      notenemy.append(name)
      
  return notenemy

