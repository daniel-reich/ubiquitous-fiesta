
def is_positive_dominant(lst):
  unique_vals = set(lst)
  pos_vals = [i for i in unique_vals if i > 0]
  neg_vals = [j for j in unique_vals if j < 0]
  return len(pos_vals) > len(neg_vals)

