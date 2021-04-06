
def adjacent_product(lst):
  L = len(lst)
  P_list = []
  while L > 1:
    P = lst[L-2]*lst[L-1]
    P_list.append(P)
    L -=1
  return (max(P_list))

