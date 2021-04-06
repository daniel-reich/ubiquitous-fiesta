
def sort_by_string(lst, txt):
  ans=[]
  for i in txt:
    for j in lst:
      if j[0]==i:
        ans.append(j)
  return ans

