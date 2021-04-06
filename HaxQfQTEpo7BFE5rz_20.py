
def alternate_pos_neg(lst):
  if any(lst[i]==0 for i in range(len(lst))):return False
  else:
    L=[lst[i]//abs(lst[i]) for i in range(len(lst))]
    return all(L[i]==L[0]*(-1)**i for i in range(1, len(lst)))

