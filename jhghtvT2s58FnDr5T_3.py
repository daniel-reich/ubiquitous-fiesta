
import copy
def jazzify(lst):
  ans=[]
  for i in lst:
    if i[-1]!="7":
      ans.append(i+"7")
    else:
      ans.append(i)
  return ans

