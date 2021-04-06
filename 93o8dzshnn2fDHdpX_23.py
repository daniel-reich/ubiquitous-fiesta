
def lst_ele_sum(lst):
  return [sum(lst[:n] + lst[n+1:]) for n in range(len(lst))]

