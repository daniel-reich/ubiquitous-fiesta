
def century(year):
  tx = str(year)
  return '21st century' if year>2000 else '{0}th century'.format(int(tx[:2])+1) if tx[-2:] != "00" else '{0}th century'.format(tx[:2])

