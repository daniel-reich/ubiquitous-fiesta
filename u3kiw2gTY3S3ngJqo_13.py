
def superheroes(heroes):
  out = []
  no = ["Wonder-Woman", "Catwoman", "Invisible-Woman"]
  for i in heroes:
    if i.endswith("man") and i not in no:
      out.append(i)
  return sorted(out)

