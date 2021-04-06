
def cap_space(txt):
  return ''.join(' '*x.isupper()+x.lower() for x in txt)

