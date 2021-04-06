
def calculate_arrowhead(lst):
  a = 0
  for l in lst:
    for x in l:
      a = a + x.count('>') - x.count('<')
  return '>'*a if a>0 else '<'*abs(a)

