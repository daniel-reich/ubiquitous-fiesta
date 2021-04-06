
def blah_blah(txt, n):
  l = txt.split()
  if n > len(l):
    return ' '.join(['blah' for e in l]) + '...'
  return ' '.join(l[:len(l)-n]) + ' ' + ' '.join(['blah' for word in l[len(l)-n:]]) + '...'

