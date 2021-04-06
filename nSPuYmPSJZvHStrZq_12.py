
def oddeven(lst):
  oddcounter = 0
  evencounter = 0
  for i in lst:
    if i % 2 == 0:
      evencounter +=1
    else:
      oddcounter+=1
  if oddcounter > evencounter:
    return True
  else:
    return False

