
def cap_to_front(s):
  small = (c for c in s if 'a' <= c <= 'z')
  big = (c for c in s if 'A' <= c <= 'Z')
  return ''.join(big) + ''.join(small)

