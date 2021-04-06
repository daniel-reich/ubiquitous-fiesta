
def split(txt):
  return ''.join(sorted(txt, key=lambda x: x.lower() not in 'aeiou'))

