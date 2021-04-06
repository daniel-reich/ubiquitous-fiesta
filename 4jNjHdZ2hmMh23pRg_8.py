
def cutting_grass(lst, *cuts):
  lsts = [[e - sum(cuts[:i+1]) for e in lst] for i in range(len(cuts))]
  return [i if all(e > 0 for e in i) else 'Done' for i in lsts]

