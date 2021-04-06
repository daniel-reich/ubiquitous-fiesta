
def sum(liste):
  erg = 0
  
  for element in liste:
    erg+= element
    
  return erg
​
def who_goes_free(n, k):
  grouplist = [1 for x in range(n)]
  pos = 0
  count = 0
  
  while sum(grouplist) != 1:  
    
    while grouplist[pos] == 0:
      if pos < len(grouplist)-1:
        pos +=1
        
      else:
        pos = 0
      
    count+=1
    
    if pos < len(grouplist)-1:
      pos+=1
      
    else:
      pos = 0
    
    if count == k:
      grouplist.pop(pos-1)
      grouplist.insert(pos-1, 0)
      count = 0
  print(grouplist.index(1))
  return grouplist.index(1)

