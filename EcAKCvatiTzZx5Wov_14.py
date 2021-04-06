
from collections import namedtuple
ColorData = namedtuple('ColorData', ['digits', 'power', 'tolerance', 'tcr'])
​
colors = {
    'black' : ColorData( 0    ,  0, None      , None       ),
    'brown' : ColorData( 1    ,  1, '+/-1%'   , '100ppm/k' ),
    'red'   : ColorData( 2    ,  2, '+/-2%'   , '50ppm/k'  ),
    'orange': ColorData( 3    ,  3, None      , '15ppm/k'  ),
    'yellow': ColorData( 4    ,  4, None      , '25ppm/k'  ),
    'green' : ColorData( 5    ,  5, '+/-0.5%' , None       ),
    'blue'  : ColorData( 6    ,  6, '+/-0.25%', '10ppm/k'  ),
    'violet': ColorData( 7    ,  7, '+/-0.1%' , '5ppm/k'   ),
    'gray'  : ColorData( 8    ,  8, '+/-0.05%', None       ),
    'white' : ColorData( 9    ,  9, None      , None       ),
    'gold'  : ColorData( None , -1, '+/-5%'   , None       ),
    'silver': ColorData( None , -2, '+/-10%'  , None       ),
}
def combine_values(seq):
  codes, total = (d.digits for d in seq), 0
  for v in codes:
    total = total * 10 + v
  return total
​
def format_resistance(val):
  prefixes = ['Ohm', 'kOhm', 'MOhm', 'GOhm' ]
  if val % 1:
    return "{:g}Ohm".format(val)
  else:
    pIdx = 0
    while val >= 1000:
      val /= 1000
      pIdx += 1
    return "{:g}{:s}".format(val, prefixes[pIdx])
​
def resistor_code(seq):
  seq = [colors[elem] for elem in seq]
  digits, seq = (seq[:2], seq[2:]) if len(seq) < 5 else (seq[:3], seq[3:])
  digits = combine_values(digits)
  res = digits * (10 ** seq[0].power)
  res = format_resistance(res)
  tol = seq[1].tolerance
  tcr = seq[2].tcr if len(seq) > 2 else None
  return res + ' ' + tol + (' ' + tcr if tcr else '')

