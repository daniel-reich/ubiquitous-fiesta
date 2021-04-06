
def bitwise_index(lst):
  memidx=-1
  for i in range(len(lst)):
    if lst[i]//2==lst[i]/2:
      if memidx==-1 or lst[memidx]<lst[i]:memidx=i
  return {"@{} index {}".format(["odd","even"][memidx//2==memidx/2],memidx): lst[memidx]} if memidx!=-1 else  "No even integer found!"

