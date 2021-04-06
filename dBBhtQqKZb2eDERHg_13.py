
def numberSequence(n):
  if n>0:
    if n==1:
      return '1'
    elif n==2:
      return '1 1'
    else:
      return str((n+1)//2)+' '+numberSequence(n-2)+' '+str((n+1)//2)
  else:
    return '-1'

