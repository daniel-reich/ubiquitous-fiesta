
def possible_path(lst):
  for i in range(1,len(lst)):
    if lst[i]==1 and lst[i-1]!=2:
      return False
    elif lst[i]==2 and lst[i-1] not in [1,'H']:
      return False
    elif lst[i]==3 and lst[i-1]!=4:
      return False
    elif lst[i]==4 and lst[i-1] not in [3,'H']:
      return False
    elif lst[i]=='H' and lst[i-1] not in [2,4]:
      return False
  return True

