
def accumulating_list(lst):
  listeFinale , sum = [] , 0
  for i in lst:
    sum += i
    listeFinale.append(sum)
  return listeFinale

