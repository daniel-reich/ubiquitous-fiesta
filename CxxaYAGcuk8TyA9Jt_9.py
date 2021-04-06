
def check_balance(expression):
  A=[]
  for i, x in enumerate(expression):
    if x=='(':
      A.append((1,i))
    elif x==')':
      A.append((-1,i))
    elif x=='{':
      A.append((2,i))
    elif x=='}':
      A.append((-2,i))
    else:
      A.append((0,i))
  B=[x for x in A if x[0]!=0]
  stack=[]
  for x in B:
    if x[0]==1 or x[0]==2:
      stack.append(x)
    else:
      if len(stack)>0 and x[0]+stack[-1][0]==0:
        stack.pop()
      else:
        return x[1]
        break
  if len(stack)==0:
    return -1
  else:
    return stack[0][1]+1

