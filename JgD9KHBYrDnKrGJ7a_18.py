
def swap_dict(dict):
  newd = {dict[i]:[] for i in dict}
  
  for i in dict:
    newd[dict[i]].append(i)
  
  return newd

