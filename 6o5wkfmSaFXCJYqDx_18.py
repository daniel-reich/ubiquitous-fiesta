
def abcmath(a, b, c):
  result=a
  i=1
  while i <= b:
    result+=result
    i+=1
  result=result%c 
  if result == 0 :
    return True
  else:
    return False

