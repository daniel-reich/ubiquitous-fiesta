
import re
def fauna_number(s):
  animals = 'muggercrocodile|one-hornedrhino|python|moth|monitorlizard|bengaltiger'
  n = list(re.findall(r'\d+(?= )', s))
  a = re.findall(r'('+animals+')', s)
  return [(x, y) for x, y in zip(a, n)]

