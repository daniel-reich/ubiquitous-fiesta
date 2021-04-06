
def count_number(l):
  l=''.join(map(str,l)).replace('[',' ').replace(']',' ').replace('.','').replace(',',' ')
  return sum(i.isdigit() for i in l.split()) if ' ' in l else len(l)

