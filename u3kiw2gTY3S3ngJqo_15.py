
def superheroes(heroes):
  return sorted([ i for i in heroes if i.endswith('man') and i not in [ "Wonder-Woman", "Catwoman", "Invisible-Woman" ]])

