
def oddeven(lst):
  def checkOdd(a):
    if a % 2 == 1:
      return True
    return False
    
  oddNum = list(filter(checkOdd, lst))
  if len(oddNum) > len(lst) // 2:
    return True
  return False

