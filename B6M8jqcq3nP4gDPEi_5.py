
def iso_group(lst, first=True):
  """The ugliest function due to ugly challenge"""
  if len(lst) < 2: return lst
  res = iso_group(lst[1:], False)
  if res[0] == lst[0]:
    res.append(lst[0])
  elif res[0] < lst[0]:
    res = [lst[0]]
  return res[0] if first and len(res)==1 else res

