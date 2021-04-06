
def chocolates_parcel(n_small, n_big, order):
    res = 0
    while order % 5 != 0 or n_big * 5 < order:
      order -= 2
      res += 1
    return res if order >= 0 and res <= n_small else -1

