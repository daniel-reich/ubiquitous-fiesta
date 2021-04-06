
def special_reverse(s, c):
  return ' '.join(k[::-1] if k[0] == c else k for k in s.split())

