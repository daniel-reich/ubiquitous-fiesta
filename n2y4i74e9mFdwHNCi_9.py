
def get_items_at(arr, par):
  if len(arr)==0 or len(arr)==1 and par=='even':
    return []
  elif len(arr)==1 and par=='odd':
    return arr
  return get_items_at(arr[:-2],par)+[arr[-1]] if par=='odd' else get_items_at(arr[:-2],par)+[arr[-2]]

