
def superheroes(heroes):
  heroines = ['Wonder-Woman', 'Catwoman', 'Invisible-Woman']
  return sorted([i for i in heroes if i[-3:] == 'man' and i not in heroines])

