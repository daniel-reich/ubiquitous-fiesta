
def row_sum(n):
  n_th_term = 0.5 * n ** 2 - 0.5 * n + 1
  
  return sum(n_th_term + i for i in range(n))

