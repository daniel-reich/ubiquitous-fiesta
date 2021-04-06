
def get_indices(lst, el):
  result = []
  for x in range(len(lst)):
    if lst[x] == el:
      result.append(x)
  return result

