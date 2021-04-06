
def split(txt):
  return ''.join([c for c in txt if c in 'aeiouAEIOU'] + [c for c in txt if c not in 'aeiouAEIOU'] )

