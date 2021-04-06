
def even_or_odd(lst):
  sumlst = sum(lst)%2
  if sumlst == 0:
    return 'even'
  else:
    return 'odd'

