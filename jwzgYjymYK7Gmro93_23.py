
def get_indices(lst, el):
  indices = []
  for i in range(len(lst)):
    if lst[i] == el:
      indices.append(i)
  return indices

