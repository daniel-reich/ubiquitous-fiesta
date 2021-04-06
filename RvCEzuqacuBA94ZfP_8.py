
def generate_hashtag(t):
  t = '#' + ''.join(s.capitalize() for s in t.split())
  return t if 1 < len(t) < 141 else False

