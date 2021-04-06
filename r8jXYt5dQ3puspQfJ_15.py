
def split(txt):
  return ''.join(sorted(txt, key=lambda a: a in 'aeiou', reverse=True))

