
def jazzify(lst):
  ans=[]
  for item in lst:
    if item and '7' not in item:
      item+='7'
      ans.append(item)
      flag=1
    else:
      ans.append(item)
  return ans

