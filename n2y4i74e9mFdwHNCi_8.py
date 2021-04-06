
def get_items_at(arr, par):
  if len(arr) == 1 and par == 'odd':
    return arr
  elif len(arr) == 3 and par == 'even':
    return [arr[-2]]
​
  cur_item = arr[-1] if par == 'odd' else arr[-2]
  if len(arr) == 2:
    return [cur_item]
  elif len(arr) > 2:
    return get_items_at(arr[:-2], par) + [cur_item]

