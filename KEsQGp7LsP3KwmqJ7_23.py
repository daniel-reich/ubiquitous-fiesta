
def check(lst):
  
  Sorted = sorted(lst)
  
  if (lst == Sorted):
    return "NO"
  
  Sample = Sorted
  
  Back = Sample[0]
  Front = Sample[1:]
    
  New = []
  New.extend(Front)
  New.append(Back)
  Sample = New
    
  if (Sample == lst):
    return "YES"
    
  while (Sample != Sorted):
    
    Back = Sample[0]
    Front = Sample[1:]
    
    New = []
    New.extend(Front)
    New.append(Back)
    Sample = New
    
    if (Sample == lst):
      return "YES"
  
  return "NO"

