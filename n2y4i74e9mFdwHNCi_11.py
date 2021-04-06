
def get_items_at(arr, par):
  if len(arr) == 1:
    return arr
  if not arr:
    return []
  if par == 'odd':
    return get_items_at(arr[:-2],'odd') + [arr[-1]]
  return get_items_at(arr[:-3],'odd') + [arr[-2]]

