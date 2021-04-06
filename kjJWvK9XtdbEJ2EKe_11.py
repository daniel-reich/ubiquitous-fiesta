
def sort_array(lst):
  result = list(range(len(lst)))
  for a in lst:
    idx = 0
    for b in lst:
      if a > b:
        idx += 1
    result[idx] = a
  return result

