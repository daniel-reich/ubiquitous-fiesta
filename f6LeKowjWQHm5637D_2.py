
def cap_to_front(s):
  return ''.join([ch for ch in s if ch.isupper()] + [ch for ch in s if ch.islower()])

