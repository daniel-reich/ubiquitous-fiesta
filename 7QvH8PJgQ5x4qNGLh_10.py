
def countdown(n, txt):
  return '{}. {}!'.format('. '.join(map(str, range(n, 0, -1))), txt.upper())

