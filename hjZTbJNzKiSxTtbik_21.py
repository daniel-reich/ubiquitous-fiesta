
def sort_by_string(lst, txt):
  ans=[]
  for i in range(len(txt)):
    for x in lst:
      if x[0]==txt[i]: ans.append(x)
  return ans

