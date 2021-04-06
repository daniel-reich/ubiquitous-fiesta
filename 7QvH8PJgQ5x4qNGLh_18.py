
def countdown(n, txt):
  count = '. '.join(list(map(str, range(1, n+1)[::-1])))
  return '{}. {}!'.format(count, txt.upper())

