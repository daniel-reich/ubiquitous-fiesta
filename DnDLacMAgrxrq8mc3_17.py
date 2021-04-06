
def blah_blah(txt, n):
  lst = txt.split(' ')
  if n > len(lst):
    return ' '.join(['blah'] * (len(lst)-1) + ['blah...'])
  else:
    return ' '.join(lst[:-n] + ['blah']*(n-1)+['blah...'])

