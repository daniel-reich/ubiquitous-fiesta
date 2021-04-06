
def is_prob_matrix(lst):
  is_square = len(lst) == len(lst[0])
  is_prob = all(0<=n<=1 for l in lst for n in l)
  is_one = all(i == 1 for i in [sum(row) for row in lst])
  return all([is_square, is_prob, is_one])

