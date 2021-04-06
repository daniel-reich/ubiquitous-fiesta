
def covered_integers(lst):
  integers = []
  for sub_lst in lst:
    integers += range(sub_lst[0], sub_lst[-1] + 1)
  return len(set(integers))

