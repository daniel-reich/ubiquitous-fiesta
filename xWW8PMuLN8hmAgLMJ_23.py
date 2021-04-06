
def postfix(expression):
  lst=expression.split()
  while len(lst)!=1:
    for i in range(len(lst)):
      if lst[i] in ['+','-','*','/']:
        lst=lst[:i-2]+[eval(str(lst[i-2])+lst[i]+str(lst[i-1]))]+lst[i+1:]
        break
  return lst[0]

