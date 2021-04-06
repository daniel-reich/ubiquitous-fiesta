
def numberSequence(n,lst=[1]):
  if n<1:
    return '-1'
  elif len(lst)==n:
    return ' '.join([str(i) for i in lst])
  elif lst[-1]>n//2:
    return numberSequence(n,[lst[0]+1]+lst)
  elif n%2==0 and lst[-1]==n//2:
    if len(lst)==n//2:
      return numberSequence(n,[1]+lst)
    else:
      return numberSequence(n,[lst[0]+1]+lst)
  return numberSequence(n,lst+[lst[-1]+1])

