
def superheroes(heroes):
  sexistHeroes = []
  for hero in heroes:
    if "man" in hero and "woman" not in hero.lower():
      sexistHeroes.append(hero)
      
  return sorted(sexistHeroes)

