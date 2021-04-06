
def ohms_law(v, r, i):
  if [v, r, i].count(None) != 1:
    return 'Invalid'
  else:
    return r * i if v == None else round(v / i, 2) if r == None else round(v / r, 2)

