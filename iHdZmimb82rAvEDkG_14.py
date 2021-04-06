
def bitwise_index(lst):
    max = None 
    for idx in range (0, len(lst)):
      nbr = lst[idx]
      if nbr/ 2 ==  nbr // 2:
        if max == None or lst[idx] >  max:
          max = lst[idx]
          indx = idx
    if  max == None:
      return "No even integer found!"
    else:
      if  indx/ 2 ==  indx // 2:
        text1 = "@even index " + str(indx) 
      else:
        text1 = "@odd index " + str(indx) 
      return {text1:max}

