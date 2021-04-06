
def dance(lst,parameter):
  if parameter == 'women':
    return [ [lst[(a+1)*-1][0] , lst[a][1] ] for a in range(len(lst))]
  elif parameter == 'men':
    return [ [lst[a][0] , lst[(a+1)*-1][1] ] for a in range(len(lst))]

