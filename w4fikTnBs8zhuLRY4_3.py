
def rep_set(n):
  def lst(lst2,k):
    if k == n:
      return lst2
    else:
      lst3 = []
      lst3.extend(lst2)
      lst3.append(lst2)
      return lst(lst3,k+1)
  return lst([],0)

