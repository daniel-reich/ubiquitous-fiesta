
def split(txt):
  is_vovel = "".join([i for i in txt if i.lower() in "aeoui"])
  res = "".join([i for i in txt if i.lower() not in "aeoui"])
  return is_vovel + res

