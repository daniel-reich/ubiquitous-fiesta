
from math import ceil
def century(year):
  suffix = 'th'
  if str(ceil(year / 100))[-1] == '1' and str(ceil(year / 100))[-2] != '1':
    suffix = 'st'
  elif str(ceil(year / 100))[-1] == '2' and str(ceil(year / 100))[-2] != '1':
    suffix = 'nd'
  elif str(ceil(year / 100))[-1] == '3' and str(ceil(year / 100))[-2] != '1':
    suffix = 'Rd'
  return str(ceil(year / 100)) + '{} century'.format(suffix)

