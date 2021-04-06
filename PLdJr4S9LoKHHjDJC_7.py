
def identify(*cube):
  sizes = list(map(lambda x: len(x),cube))
  if len(set(sizes)) == 1:
    return 'Full' if sizes[0] == len(cube) else 'Non-Full'
  return 'Missing {}'.format(str(sizes.count(min(sizes))))

