
def to_list(dct):
  ans=[]
  for k in dct.keys():
    ans.append([k,dct[k]])
  return sorted(ans)

