
def num_in_str(lst):
  ret=[]
  for i in range(len(lst)):
    for j in lst[i]:
      if j.isdigit() and lst[i] not in ret:
        ret.append(lst[i])
  return ret

