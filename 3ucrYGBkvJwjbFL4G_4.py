
def reversible_inclusive_list(s, e):
  if s==e: return [s]
  elif s<e: return [s] + reversible_inclusive_list(s+1, e)
  else: return [s] + reversible_inclusive_list(s-1, e)

