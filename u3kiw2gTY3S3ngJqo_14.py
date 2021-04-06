
def superheroes(heroes):
  return sorted([x for x in heroes if x.endswith("man") and not x.lower().endswith("woman")])

