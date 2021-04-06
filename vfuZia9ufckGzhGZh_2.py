
def seq_level(lst):
  dif1 = [j - i for i, j in zip(lst, lst[1:])]
  dif2 = [j - i for i, j in zip(dif1, dif1[1:])]
  dif3 = [j - i for i, j in zip(dif2, dif2[1:])]
  
  if not sum(dif2) : return 'Linear'
  if not sum(dif3) : return 'Quadratic'
  return 'Cubic'

