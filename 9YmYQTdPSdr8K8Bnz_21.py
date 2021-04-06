
def unique_lst(lst):
  resp = []
  if len(lst) == 0:
    return []
  else:
    for i in lst:
      if i > 0 and i not in resp:
        resp.append(i)
  return resp

