
def postfix(expr):
  lst=expr.split(' ')
  while(len(lst)>1):
    for i in range(0,len(lst)):
      if(lst[i] in "+-*/"):
        k=str(eval(lst[i-2]+lst[i]+lst[i-1]))
        lst=lst[0:i-2]+[k]+lst[i+1:]
        break
  return int((lst[0].split('.'))[0])

