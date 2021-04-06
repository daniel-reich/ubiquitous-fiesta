
def order(lst):
  ordered = sorted(lst)
  indices = list(map(lambda e: lst.index(e), ordered))
  
  current = None
  slice_idx = 0
  for idx, value in list(enumerate(indices)):
    if current != value:
      current = value
      slice_idx = value
      continue
    
    new_idx = lst.index(lst[value], slice_idx + 1)
    slice_idx = new_idx
    indices[idx] = new_idx
    
  return indices

