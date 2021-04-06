
def pos_neg_sort(lst):
  pos = sorted([i for i in lst if i>0],reverse=True)
  return [pos.pop() if j>0 else j for j in lst]

