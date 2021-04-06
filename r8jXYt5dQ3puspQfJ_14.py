
def split(txt):
  return ''.join([''.join([a for a in txt if a in 'aeiouAEIOU']), ''.join([b for b in txt if b not in 'aeiouAEIOU'])])

