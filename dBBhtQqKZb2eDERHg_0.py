
def numberSequence(n):
  if n<1: return '-1'
  if n<3: return ' '.join(['1']*n)
  return '{} {} {}'.format(str((n+1)//2),numberSequence(n-2),str((n+1)//2))

