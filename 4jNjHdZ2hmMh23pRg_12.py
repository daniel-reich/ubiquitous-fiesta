
def cutting_grass(lst, *cuts):
  return [[x-sum(cuts[:i+1]) for x in lst] if min(lst)-sum(cuts[:i+1])>0 \
          else 'Done' for i in range(len(cuts))]

