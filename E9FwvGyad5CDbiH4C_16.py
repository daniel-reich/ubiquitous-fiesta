
def block(lst):
  TotR=len(lst)
  Ones=0
  for C in range(len(lst[0])):
    Flag=0
    for R in range(TotR):
      if lst[R][C]==2:Flag=1
      if lst[R][C]==1 and Flag:Ones+=1
  return Ones

