
def is_prob_matrix(lst):
  return len(lst) == len(lst[0]) and \
         all(0 <= x <= 1 for y in lst for x in y) and \
         all(sum(y) == 1 for y in lst)

