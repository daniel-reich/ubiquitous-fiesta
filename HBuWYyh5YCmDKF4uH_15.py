
def almost_sorted(lst):
  diff_1 = [i-j for i, j in zip(lst[1:],lst[:-1]) if (i-j) < 0]
  diff_2 = [j-i for i, j in zip(lst[1:],lst[:-1]) if (j-i) < 0]
  if any([len(diff_1) == 1, len(diff_2) == 1]): return True
  return False

