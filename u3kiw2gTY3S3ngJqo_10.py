
def superheroes(heroes):
  return sorted([i for i in heroes if i.endswith("man") and not i.lower().endswith("woman")])

