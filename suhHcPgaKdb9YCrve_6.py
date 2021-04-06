
def even_or_odd(s):
  I=[int(x) for x in s]
  E=[x for x in I if x%2==0]
  O=[x for x in I if x%2]
  if sum(E)==sum(O):
    return 'Even and Odd are the same'
  elif sum(E)>sum(O):
    return 'Even is greater than Odd'
  else:
    return 'Odd is greater than Even'

