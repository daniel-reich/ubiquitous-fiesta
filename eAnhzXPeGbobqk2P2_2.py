
def century(year):
  return '{}th century'.format((year+99)//100) if year<2001 else '21st century'

