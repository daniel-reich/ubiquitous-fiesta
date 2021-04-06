
def superheroes(heroes):
  return sorted(x for x in heroes if x.lower()[-3:]=="man" and x.lower()[-5:]!="woman")

