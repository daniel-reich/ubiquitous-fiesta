
def ohms_law(v, r, i):
  if r and i and not v:
    ans = round(r * i, 2)
  elif v and i and not r:
    ans = round(v / i, 2)
  elif v and r and not i:
    ans = round(v / r, 2)
  else:
    ans = 'Invalid'
  return ans

