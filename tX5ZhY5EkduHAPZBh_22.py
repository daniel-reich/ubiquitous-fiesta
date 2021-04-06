
def nearest_element(n, lst):
  distances = [abs(x - n) for x in lst]
  nearest = min(distances)
  start_idx = distances.index(nearest)
  end_idx = distances[::-1].index(nearest)
  if start_idx + end_idx == len(lst) - 1:
    return start_idx
  else:
    first_num = lst[start_idx]
    last_num = lst[len(lst) - 1 - end_idx]
    return lst.index(max(first_num, last_num))

