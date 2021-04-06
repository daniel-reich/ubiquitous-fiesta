
def superheroes(heroes):
  man = [x for x in heroes if x.lower().endswith('man')]
  only = [x for x in man if not x.lower().endswith('woman')]
  return sorted(only)

