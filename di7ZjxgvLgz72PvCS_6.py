
def validate_swaps(lst, txt):
  model=','.join(txt).split(',')
  newls=[]
  lss=[]
  result=[]
  for i in range(len(txt)):
    for c in range(1,len(txt)):
      t=model[i]
      model[i]=model[c]
      model[c]=t
      newls.append(model)
      model=','.join(txt).split(',')
  for i in newls:
    lss.append(''.join(i))
  for i in lst:
    if i in lss:
      result.append(True)
    else:
      result.append(False)
  return result

