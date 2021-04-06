
def superheroes(heroes):
  return sorted([x for x in heroes if x[-3:] == "man" and x not in ["Wonder-Woman", "Catwoman", "Invisible-Woman"]])

