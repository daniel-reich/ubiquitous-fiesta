
def swap_dict(info):
  result = {}
  for k, v in info.items():
    if v in result:
      result[v].append(k)
    else:
      result.update({v: [k]})
  return result

