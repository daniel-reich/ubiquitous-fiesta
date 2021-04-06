
def final_result(lst):
  ret = []
  prev = None
  for l in lst:
    if l == prev:
      if len(ret): ret.pop()
      continue
    else:
      ret.append(l)
      prev = l
      
  return ret if ret == lst else final_result(ret)

