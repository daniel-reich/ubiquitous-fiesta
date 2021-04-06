
def dance(lst,parameter):
  if parameter == 'men':
    length = len(lst)
    if length%2 == 0:
      for i in range(0,length//2):
        lst[i][1],lst[-(i+1)][1] = lst[-(i+1)][1],lst[i][1]
      return lst
    else:
      for i in range(0,length//2):
        lst[i][1],lst[-(i+1)][1] = lst[-(i+1)][1],lst[i][1]
      return lst
  elif parameter == 'women':
    length = len(lst)
    if length%2 == 0:
      for i in range(0,length//2):
        lst[i][0],lst[-(i+1)][0] = lst[-(i+1)][0],lst[i][0]
      return lst
    else:
      for i in range(0,length//2):
        lst[i][0],lst[-(i+1)][0] = lst[-(i+1)][0],lst[i][0]
      return lst

