
def mySort(files, sort):
  same = [item for item in files if item.split('.')[sort] == files[sort].split('.')[sort]]
  different = [item for item in files if item not in same]
  return same, different
  
def clean_up(files, sort):
  
  myList = []
  sortDict =  {'prefix':0, 'suffix':1}
  x = sortDict[sort]
  
  for i in range(5):
    s, d = mySort(files, x)
    myList.append(s)
    files = d
  
  return [item for item in myList if len(item) > 0]

