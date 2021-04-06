
def find_the_falsehoods(lst):
  new = []
  for i in lst:
    if i:
      continue
    
    elif not i:
        new.append(i)
  return new

