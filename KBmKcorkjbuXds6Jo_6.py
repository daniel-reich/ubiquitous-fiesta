
def chocolates_parcel(n_small, n_big, order):
  for b_count in range(n_big, -1, -1):
    rem = order - (5 * b_count)
    if rem >= 0 and rem % 2 == 0 and rem / 2 <= n_small:
      return rem / 2
  return -1

