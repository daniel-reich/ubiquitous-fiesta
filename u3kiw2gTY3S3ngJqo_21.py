
def superheroes(heroes):
  l = [i for i in heroes if i.endswith("man")]
  final = [i for i in l if not i.endswith(("Woman","woman"))]
  return sorted(final)

