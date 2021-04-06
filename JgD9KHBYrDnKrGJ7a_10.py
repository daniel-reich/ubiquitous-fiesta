
def swap_dict(d):
  ans = {}
  for k, v in d.items():
    x = ans.get(v, []) + [k]
    ans.update({v: x})
  return ans

