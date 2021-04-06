
def diag_dom(lst):
 dom=True
 for i in range(0,len(lst)):
  total=0
  for k in range(0,len(lst[i])):
   total+=abs(lst[i][k])
  #print('total',total)
  #print('lst[i][i]',lst[i][i])
  if abs(lst[i][i]) <= total-abs(lst[i][i]):
   dom=False
   break
 return dom

