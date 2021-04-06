
def evaluate_polynomial(poly, num):
  x= num; pos = []
  for change in [('^', '**'),('(', '*('),('//', '//^')]:
    s = 0
    while s >= 0:
      s = poly.find(change[0], s)
      if s != -1: poly = poly[:s]+change[1]+poly[s+1:]; s=s+2
  for let in enumerate(poly[:-1]):
    if let[1].isnumeric() and poly[let[0]+1] == 'x': pos.append(let[0]+1)
  while pos: change = pos.pop(); poly = poly[:change]+'*'+poly[change:]
  try: return eval(poly)
  except: return "invalid"

