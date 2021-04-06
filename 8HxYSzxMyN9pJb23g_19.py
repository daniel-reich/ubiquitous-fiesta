
def split_n_cases(txt, cases):
  ans  = []
  if len(txt)%cases == 0:
    div = len(txt)//cases
    ind1 = 0
    ind2 = div
    for i in range(cases):
      ans.append(txt[ind1:ind2])
      ind1 += div
      ind2 += div 
  else:
    ans.append("Error")
  return ans

