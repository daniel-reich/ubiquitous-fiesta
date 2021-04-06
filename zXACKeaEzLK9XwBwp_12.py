
def split_bunches(lst):
 op=[]
 for l in range(len(lst)):
  for i in range((lst[l]['quantity'])):
         newdict=lst[l].copy()
         newdict['quantity']=1
         op.append(newdict)
  newdict={}
 return op

