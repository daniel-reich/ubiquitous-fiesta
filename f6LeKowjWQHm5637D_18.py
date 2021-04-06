
def cap_to_front(s):
  return ''.join([c for c in s if c.isupper()] + [c for c in s if c.islower()])

