
def is_prob_matrix(arr):
  sq_cond = len(arr) == len(arr[0])
  entry_cond = all(0<=e<=1 for e in sum(arr,[]))
  sum_cond = all(sum(row) == 1 for row in arr)
  return sq_cond and entry_cond and sum_cond

