
def rank(lst):
  sorted_lst = sorted(lst)
  return [mean_(sorted_lst, e) for e in lst]
  
def mean_(lst, elem):
  i_lst = [i for i, e in enumerate(lst) if e == elem]
  return 1.0 * sum(i_lst) / len(i_lst)

