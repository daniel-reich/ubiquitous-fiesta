
def diag_dom(lst):
  return all([2*abs(j[i])>sum(abs(k) for k in j) for i,j in enumerate(lst)])

