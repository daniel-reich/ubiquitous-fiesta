
def pairwise_swap(lst):
  for i in range(0, len(lst)-1, 2):
    lst[i], lst[i+1] = lst[i+1], lst[i]
  if len(lst) % 2:
    ascii_val_at_idx = lambda i: sum(ord(c) for c in str(lst[i]))
    swp_idx = max(range(len(lst)), key=ascii_val_at_idx)
    lst[-1], lst[swp_idx] = lst[swp_idx], lst[-1]
  return lst

