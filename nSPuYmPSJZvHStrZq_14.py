
def oddeven(lst):
  for i in range(len(lst)):
    a=0
    b=0
    if lst[i]%2==0:
      a+=1
    else:
      b+=1
    if b>a:
      return True
    return False

