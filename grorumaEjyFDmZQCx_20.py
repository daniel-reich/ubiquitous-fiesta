
def is_wristband(lst):
  
  for i in lst:
    print(i)
  horizontal=lst
  horizontal=[i for i in horizontal if len(set(i))==1]
  if len(horizontal)==len(lst): 
    print('check')
    return True
  vertical=set([str(i) for i in lst])
  if len(vertical)==1: return True
  rightdiag=True
  for i in range(len(lst)-1):
    for x in range(len(lst[i])-1):
      if lst[i][x]!=lst[i+1][x+1]: 
        print(lst[i][x],lst[i+1][x+1])
        rightdiag=False
        break
    if rightdiag==False: break
  if rightdiag==True: 
    return True
  leftdiag=True
  for i in range(len(lst)-1):
    for x in range(1,len(lst[i])):
      if lst[i][x]!=lst[i+1][x-1]: 
        print(lst[i][x],lst[i+1][x-1])
        leftdiag=False
        break
      print(lst[i][x],lst[i+1][x-1])
    if leftdiag==False: break
  if leftdiag==True: return True
  return False

