
def eval_algebra(eq):
  lst=eq.split(' ')
  if lst[-1]=='x':
    if lst[1]=='+':
      x=eval(lst[0])+eval(lst[2])
    else:
      x=eval(lst[0])-eval(lst[2])
  else:
    if lst[0]=='x':
      if lst[1]=='+':
        x=eval(lst[-1])-eval(lst[2])
      else:
        x=eval(lst[-1])+eval(lst[2])
    else:
      if lst[1]=='+':
        x=eval(lst[-1])-eval(lst[0])
      else:
        x=eval(lst[0])-eval(lst[-1])
  return x

