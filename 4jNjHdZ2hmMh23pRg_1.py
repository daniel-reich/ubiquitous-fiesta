
def cutting_grass(lst, *cuts):
  return [[i-sum(cuts[:j+1]) for i in lst] if min(lst)>sum(cuts[:j+1]) else 'Done' for j in range(len(cuts))]

