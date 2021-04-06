
def cms_selector(lst, txt):
  ans=[]
  for i in lst:
    if txt in i:
      ans.append(i)
  return sorted(ans)

