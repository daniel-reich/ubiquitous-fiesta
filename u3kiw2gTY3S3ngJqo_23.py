
def superheroes(lst):
  l = [i for i in lst if i.lower()[-3:] == "man" and i.lower()[-5:] != "woman"]
  return sorted(l)

