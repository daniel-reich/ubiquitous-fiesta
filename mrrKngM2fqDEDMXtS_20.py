
def can_patch(bridge, planks):
  planks=sorted(planks)
  bridge=''.join([str(i) for i in bridge]).replace('1',' ').split()
  bridge=[i for i in bridge if i!='0']
  print(bridge,planks)
  for x in bridge:
    cancross=False
    ind=-1
    for i in range(len(planks)):
      if planks[i]>=len(x)-1 and planks[i]<=len(x):
        cancross=True
        ind=i
        break
    if cancross==False: return False
    else: planks[ind]=0
  return True

