
def cap_space(txt):
  return ''.join(c if c.islower() else ' '+c.lower() for c in txt)

