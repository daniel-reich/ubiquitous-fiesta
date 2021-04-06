
def superheroes(heroes):
  return sorted(filter(lambda x:x[-3:]=="man" and "woman" not in x.lower(), heroes))

