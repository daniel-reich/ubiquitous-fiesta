
def get_items_at(arr, par, n = -1):
  if abs(n) == len(arr):
    if abs(n) % 2 == 0 and par == 'even' or abs(n) % 2 == 1 and par == 'odd':
      return [arr[n]]
    else:
      return []
  if abs(n) % 2 == 0 and par == 'even' or abs(n) % 2 == 1 and par == 'odd':
    return get_items_at(arr, par, n-1) + [arr[n]]
  else:
    return get_items_at(arr, par, n-1)

