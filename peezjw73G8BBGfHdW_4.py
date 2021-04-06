
def arithmetic_operation(n):
​
  lst=list(n.split(' '))
  if lst[1]=='+':
    return (int(lst[0])+int(lst[2]))
  elif lst[1]=='-':
    return (int(lst[0])-int(lst[2]))
  elif lst[1]=='/':
    if int(lst[2])!= 0:
      return (int(lst[0])/int(lst[2]))
    else:
      return (-1)
  else:
    return (int(lst[0])*int(lst[2]))

