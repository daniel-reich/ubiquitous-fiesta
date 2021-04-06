
def filter_list(lst):
    newList = []
    for l in lst:
      if type(l) is int:
        newList.append(l)
    
    return newList

