
def mumbling(s):
  return '-'.join(((i + 1) * j).title() for i, j in enumerate(s))

