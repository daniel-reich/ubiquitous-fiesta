
def get_items_at(arr, par, res = []):
  if len(arr) == 0:
      return res[::-1]
  if par == "odd":
    if len(arr) == 1:
      res.append(arr[0])
      return res[::-1]
    else:
      return get_items_at(arr[:-2], par, res + [arr[-1]])
  else:   
    if len(arr) == 1:
      return res[::-1]
    else:
      return get_items_at(arr[:-2], par, res + [arr[-2]])

