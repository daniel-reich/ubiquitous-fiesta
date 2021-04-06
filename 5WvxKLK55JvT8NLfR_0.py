
def diag_dom(ar):
  return all(2*abs(ar[i][i])>sum(abs(e) for e in ar[i]) for i in range(len(ar)))

