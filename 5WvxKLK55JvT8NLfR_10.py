
def diag_dom(lst):
  lst =[[abs(x) for x in l] for l in lst]
  return all([lst[i][i]*2>sum(lst[i]) for i in range(len(lst))])

