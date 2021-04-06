
def swap_d(k, v, swapped):
  dic = {}
  if(swapped):
    index = 0
    while index < len(k):
      dic[v[index]] = k[index]
      index += 1
  else:
    index = 0
    while index < len(k):
      dic[k[index]] = v[index]
      index += 1
  return dic

