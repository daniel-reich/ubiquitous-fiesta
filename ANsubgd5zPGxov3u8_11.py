
def initialize(names):
  res = []
  for name in names:
    initials = ""
    for word in name.split(' '):
      initials = initials + word[0].upper() + ". "
    res.append(initials.strip())
  return res

