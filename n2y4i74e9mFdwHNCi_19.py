
def get_items_at(arr, par):
  if arr==None or len(arr)==0:return []
  if par=='odd': return get_items_at(arr[:-1], 'even') + [arr[-1]]
  return get_items_at(arr[:-1], 'odd')

