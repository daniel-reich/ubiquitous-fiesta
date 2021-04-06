
def last_ancestor(folders,X,Y):
  def previous(K):
    above_K, current = [K], K
    while True:
      previous = [Z for Z in folders if current in folders[Z]]
      if previous:
        above_K+= [previous[0]]
        current = previous[0]
      else: return above_K
  
  return [Z for Z in previous(X) if Z in previous(Y)][0]

