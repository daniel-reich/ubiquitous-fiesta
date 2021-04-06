
def find_the_falsehoods(lst):
  ko=[]
  
  for i in lst:
    if i in (0,"",(),[],{},None):
      ko.append(i)
      
  return ko

