
def superheroes(heroes):
  lst = []
  for hero in heroes:
    if 'man' in hero.lower() and not 'woman' in hero.lower():
      lst.append(hero)
  return sorted(lst)

