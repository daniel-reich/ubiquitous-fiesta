
def cap_to_front(s):
  return ''.join(sorted(s, key=str.isupper, reverse=True))

