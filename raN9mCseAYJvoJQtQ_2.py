
def remove_empty_arrays(arr):
  lst = []
  for x in arr:
    if x != []:
      lst.append(x)
  return lst

