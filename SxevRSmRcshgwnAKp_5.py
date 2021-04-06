
def pricey_prod(d):
  return sorted([pr for pr in d if d[pr]>=500], key = lambda pr:-d[pr])

