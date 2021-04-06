
def cutting_grass(lst, *cuts):
  ans=[]
  done=False
  for i in cuts:
    lst=[x-i for x in lst]
    for x in lst:
      if x<=0: done=True
    if done==False: ans.append(lst)
    if done:
      ans.append('Done')
  return ans

