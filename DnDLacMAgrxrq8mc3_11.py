
def blah_blah(txt, n):
  a = txt.split()
​
  if len(a) < n:
    return ' '.join(['blah' for i in a]) + '...'
    
  b = ' '.join([x for i, x in enumerate(a) if i < len(a)-n])  
  return '{}{}...'.format(b, ' blah'*n)

