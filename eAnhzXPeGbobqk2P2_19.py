
import math
def century(year):
  dc = str(math.ceil(year/100))
  return (dc + 'st century') if dc == '21' else (dc + 'th century')

