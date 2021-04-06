
def initialize(names):
  res = []
  for name in names:
    first, last = name.split()
    res.append(first[0] + ". " + last[0] + ".")
  return res

