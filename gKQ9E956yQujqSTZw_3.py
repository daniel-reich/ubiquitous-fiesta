
def num_to_dict(lst):
  res = []
  for el in lst:
    res.append({str(el):chr(el)})
  return res

