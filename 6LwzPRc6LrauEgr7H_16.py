
def worm_length(worm):
  if not len(worm): return 'invalid'
  size = 0
  for c in worm:
    if c != '-':
      return 'invalid'
    size += 10
  return str(size) + ' mm.'

