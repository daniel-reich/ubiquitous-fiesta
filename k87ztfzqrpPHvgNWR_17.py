
def widen_streets(lst, n):
  streets = ['#' in i for i in zip(*lst)]
  new_lst = [''.join(lst[i][j] if streets[j] else ' '*n for j in range(len(lst[0]))) for i in range(len(lst))]
  return new_lst

