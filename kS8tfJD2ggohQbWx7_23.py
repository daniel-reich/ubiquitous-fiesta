
def last_name_lensort(names):
  names = sorted(names, key=lambda x: x.split(" ")[1])
  return sorted(names, key=lambda x: len(x.split(" ")[1]))

