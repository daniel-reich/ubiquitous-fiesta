
def get_items_at(arr, par,n=1):
  if not arr:
    return []
  if (n&1 and par == 'odd') or (not n&1 and par == 'even'):
    return get_items_at(arr[:-1],par,n+1)+[arr[-1]]
  else:
    return get_items_at(arr[:-1],par,n+1)

