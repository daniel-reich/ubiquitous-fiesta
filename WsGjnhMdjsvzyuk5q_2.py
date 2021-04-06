
def dashed(txt):
  return ''.join('-{}-'.format(l) if l.lower() in 'aeiou' else l for l in txt)

